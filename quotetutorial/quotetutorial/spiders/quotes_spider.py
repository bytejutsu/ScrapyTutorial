import scrapy
from ..items import QuotetutorialItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):

        quoteTutorialItem = QuotetutorialItem()

        all_div_quotes = response.css('div.quote')

        for quote in all_div_quotes:
            title = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tag = quote.css('.tag::text').extract()

            quoteTutorialItem['title'] = title
            quoteTutorialItem['author'] = author
            quoteTutorialItem['tag'] = tag

        yield quoteTutorialItem
