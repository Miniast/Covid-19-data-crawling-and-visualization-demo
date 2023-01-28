import copy
import re
import scrapy
from vaccine.http import MyRequest
from vaccine.items import VaccineItem


class VaccinespiderSpider(scrapy.Spider):
    name = 'vaccineSpider'
    allowed_domains = ['ourworldindata.org']
    start_urls = [
        'https://ourworldindata.org/explorers/coronavirus-data-explorer?tab=table&time=2021-12-20&facet=none&Metric=People+vaccinated&Interval=Cumulative&Relative+to+Population=false&Color+by+test+positivity=false&country=USA~ITA~CAN~DEU~GBR~FRA']
    next_url = 'https://ourworldindata.org/explorers/coronavirus-data-explorer?tab=table&time=2021-12-20&facet=none&Metric=People+vaccinated&Interval=Cumulative&Relative+to+Population=true&Color+by+test+positivity=false&country=USA~ITA~CAN~DEU~GBR~FRA'

    def start_requests(self):
        for url in self.start_urls:
            yield MyRequest(url=url, callback=self.parse, dont_filter=True, cb_kwargs={'rate_info': 0})

    def parse(self, response, **kwargs):
        item = VaccineItem()

        vaccine_table = response.xpath('/html/body/main/div/div[3]/div/div[1]/div/table/tbody')
        now_id = 1
        now_area_name = vaccine_table.xpath(f'./tr[{now_id}]/td[1]/text()').get()
        while now_area_name is not None:
            item['area_name'] = now_area_name
            tmp = vaccine_table.xpath(f'./tr[{now_id}]/td[2]/text()').get()
            if kwargs['rate_info'] == 0:
                item['tot_vaccined'] = vaccine_table.xpath(f'./tr[{now_id}]/td[2]/text()').get()
            else:
                item['tot_vaccined_rate'] = vaccine_table.xpath(f'./tr[{now_id}]/td[2]/text()').get()
            now_id += 1
            now_area_name = vaccine_table.xpath(f'./tr[{now_id}]/td[1]/text()').get()
            yield item

        if kwargs['rate_info'] == 0:
            next_page_url = self.next_url
            yield MyRequest(url=next_page_url, callback=self.parse, dont_filter=True,
                            cb_kwargs={'rate_info': 1})
        pass
