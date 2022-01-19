# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotetutorialItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()


class AmazonItem(scrapy.Item):
    product_name = scrapy.Field()
    product_price = scrapy.Field()
    product_price = scrapy.Field()
    product_imagelink = scrapy.Field()

