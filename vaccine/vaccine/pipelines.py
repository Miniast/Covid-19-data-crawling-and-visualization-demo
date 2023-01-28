# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class VaccinePipeline:
    fieldname = ['area_name', 'tot_vaccined', 'tot_vaccined_rate']

    def __init__(self):
        self.file = open('result.csv', 'w', newline='')
        self.writer = csv.DictWriter(self.file, self.fieldname)
        self.writer.writeheader()

    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item

    def close_spider(self, spider):
        self.file.close()
