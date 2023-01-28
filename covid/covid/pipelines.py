# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CovidPipeline:
    fieldname = ['area_id', 'area_name', 'date', 'tot_confirmed', 'new_confirmed', 'tot_deaths', 'death_rate',
                 'affected_population_rate']

    def __init__(self):
        self.file = open('result.csv', 'w', newline='')
        self.writer = csv.DictWriter(self.file, self.fieldname)
        self.writer.writeheader()

    def process_item(self, item, spider):
        info = {'area_id': item['area_id'], 'area_name': item['area_name']}
        for i in range(len(item['covid_info'])):
            info['date'] = item['covid_info'][i]['date']
            info['tot_confirmed'] = item['covid_info'][i]['tot_confirmed']
            info['new_confirmed'] = item['covid_info'][i]['new_confirmed']
            info['tot_deaths'] = item['covid_info'][i]['tot_deaths']
            info['death_rate'] = item['covid_info'][i]['death_rate']
            info['affected_population_rate'] = item['covid_info'][i]['affected_population_rate']
            self.writer.writerow(info)
        return item

    def close_spider(self, spider):
        self.file.close()
