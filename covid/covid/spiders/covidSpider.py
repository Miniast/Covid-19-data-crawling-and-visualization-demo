import copy
import re
import scrapy
from covid.http import MyRequest
from covid.items import CovidItem


def get_integer(myinfo):
    if myinfo is not None:
        return int(''.join(c for c in str(myinfo) if c.isdigit()))
    else:
        return None


def get_float(myinfo):
    if myinfo is not None:
        return float(re.findall(r"\d+\.?\d*", str(myinfo))[0])
    else:
        return None


class CovidspiderSpider(scrapy.Spider):
    name = 'covidSpider'
    start_urls = ['https://covid.observer']
    area_abbr_list = ['World']
    area_name_list = ['World']

    def start_requests(self):
        for url in self.start_urls:
            yield MyRequest(url=url, callback=self.parse, dont_filter=True, cb_kwargs={'now_area_id': 0})

    def parse(self, response, **kwargs):
        item = CovidItem()
        info = response.xpath('//table/tbody')
        now_id = 1

        if info.xpath(f'./tr[{now_id}]/td[1]/text()').get() is not None:
            date_time = str(info.xpath(f'./tr[{now_id}]/td[1]/text()').get())
            while re.match("Dec", date_time) is None or not 5 <= int(re.findall('\d+', date_time)[0]) <= 20:
                now_id += 1
                date_time = str(info.xpath(f'./tr[{now_id}]/td[1]/text()').get())
            limit_id = now_id + 15
            daily_info = {}
            daily_info_list = []
            item['area_id'] = kwargs['now_area_id']
            item['area_name'] = self.area_name_list[kwargs['now_area_id']]

            while now_id <= limit_id:
                daily_info['date'] = info.xpath(f'./tr[{now_id}]/td[1]/text()').get()
                daily_info['tot_confirmed'] = get_integer(info.xpath(f'./tr[{now_id}]/td[2]/text()').get())
                pre_confirmed = get_integer(info.xpath(f'./tr[{now_id + 1}]/td[2]/text()').get())
                if daily_info['tot_confirmed'] is not None and pre_confirmed is not None:
                    daily_info['new_confirmed'] = daily_info['tot_confirmed'] - pre_confirmed
                else:
                    daily_info['new_confirmed'] = None
                daily_info['tot_deaths'] = get_integer(info.xpath(f'./tr[{now_id}]/td[5]/text()').get())
                daily_info['death_rate'] = get_float(info.xpath(f'./tr[{now_id}]/td[8]/text()').get())
                daily_info['affected_population_rate'] = get_float(info.xpath(f'./tr[{now_id}]/td[9]/text()').get())
                daily_info_list.append(copy.deepcopy(daily_info))
                now_id += 1
            item['covid_info'] = daily_info_list
            yield item

        if kwargs['now_area_id'] == 0:
            self.area_abbr_list.extend(response.xpath(f'/html/body/div[10]/div[2]/p/a/@href').extract())
            self.area_name_list.extend(response.xpath(f'/html/body/div[10]/div[2]/p/a/text()').extract())
            next_page_url = self.start_urls[0] + self.area_abbr_list[kwargs['now_area_id'] + 1]
            yield MyRequest(url=next_page_url, callback=self.parse, dont_filter=True,
                            cb_kwargs={'now_area_id': kwargs['now_area_id'] + 1})
        elif kwargs['now_area_id'] + 1 < len(self.area_abbr_list):
            next_page_url = self.start_urls[0] + self.area_abbr_list[kwargs['now_area_id'] + 1]
            yield MyRequest(url=next_page_url, callback=self.parse, dont_filter=True,
                            cb_kwargs={'now_area_id': kwargs['now_area_id'] + 1})
        pass
