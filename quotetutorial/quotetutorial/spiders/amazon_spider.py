import scrapy
from ..items import AmazonItem


class AmazonSpider(scrapy.Spider):

    name = 'amazon'
    start_urls = [
        'https://www.amazon.com/s?rh=n%3A154606011&fs=true&ref=lp_154606011_sar'
    ]

    def parse(self, response):

        item = AmazonItem()
        product_name = response.css('.a-color-base.a-text-normal::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base.a-color-base').css('::text').extract()
        product_price = response.css('.a-price span span').css('::text').extract()
        product_imagelink = response.css('.s-image::attr(src)').extract()

        item['product_name'] = product_name
        item['product_author'] = product_author
        item['product_price'] = product_price
        item['product_imagelink'] = product_imagelink

        yield item


