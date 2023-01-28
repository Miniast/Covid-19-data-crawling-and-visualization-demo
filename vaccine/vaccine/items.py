# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VaccineItem(scrapy.Item):
    area_name = scrapy.Field()
    tot_vaccined = scrapy.Field()
    tot_vaccined_rate = scrapy.Field()
    pass
