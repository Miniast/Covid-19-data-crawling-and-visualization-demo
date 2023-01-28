# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CovidItem(scrapy.Item):
    area_id = scrapy.Field()
    area_name = scrapy.Field()
    covid_info = scrapy.Field()
    # new_cases = scrapy.Field()
    # tot_cases = scrapy.Field()
    # new_deaths = scrapy.Field()
    # tot_deaths = scrapy.Field()
    # new_recovered = scrapy.Field()
    # tot_recovered = scrapy.Field()
    # active_cases = scrapy.Field()
    pass
