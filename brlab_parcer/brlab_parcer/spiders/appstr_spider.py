# -*- coding: utf-8 -*-
import scrapy


class AppstrSpiderSpider(scrapy.Spider):
    name = 'appstr'
    start_urls = [
        'https://apps.apple.com/ru/app/лига-ставок-ставки-на-спорт/id1065803457'
    ]


    def parse(self, response):
        for block in response.css('.we-customer-review'):
            yield {
                    'review_title': block.css('h3.we-customer-review__title').get(),
                    'review_description': block.css('.we-customer-review__title+ .we-customer-review__body').get(),
                    'user_name': block.css('.we-customer-review__user::text').get(),
                    'review_data': block.css('.we-customer-review__date::text').get(),
                }
