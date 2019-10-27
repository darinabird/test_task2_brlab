# -*- coding: utf-8 -*-
import scrapy


class AppstrSpiderSpider(scrapy.Spider):
    name = 'appstr'
    start_urls = [
        'https://apps.apple.com/ru/app/%D0%BB%D0%B8%D0%B3%D0%B0-%D1%81%D1%82%D0%B0%D0%B2%D0%BE%D0%BA-%D1%81%D1%82%D0%B0%D0%B2%D0%BA%D0%B8-%D0%BD%D0%B0-%D1%81%D0%BF%D0%BE%D1%80%D1%82/id1065803457'
    ]


    def parse(self, response):
        for block in response.css('.we-customer-review'):
            yield {
                    'review_title': block.css('h3.we-customer-review__title::text').get(),
                    'review_description': block.css('.we-customer-review__title+ .we-customer-review__body p::text').get(),
                    'user_name': block.css('.we-customer-review__user::text').get(),
                    'review_data': block.css('.we-customer-review__date::text').get(),
                }
