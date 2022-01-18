import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import QuotetutorialItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    page_number = 0
    start_urls = [
        'http://quotes.toscrape.com/login',
    ]

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username': 'admin',
            'password': 'admin'
        }, callback=self.start_scraping)

    def start_scraping(self, response):
        # open_in_browser(response)

        quote_tutorial_item = QuotetutorialItem()

        all_div_quotes = response.css('div.quote')

        for quote in all_div_quotes:
            title = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tags = quote.css('.tag::text').extract()

            quote_tutorial_item['title'] = title
            quote_tutorial_item['author'] = author
            quote_tutorial_item['tags'] = tags

            yield quote_tutorial_item

        next_page = f'http://quotes.toscrape.com/page/{QuoteSpider.page_number}/'

        if QuoteSpider.page_number < 12:
            QuoteSpider.page_number += 1
            yield response.follow(next_page, callback=self.start_scraping)
