# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ToscrapeeItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()

    """
    rating = scrapy.Field()
    paragraph = scrapy.Field()
    upc = scrapy.Field()
    product_type = scrapy.Field()
    price_witout_tax = scrapy.Field()
    price_with_tax = scrapy.Field()
    tex = scrapy.Field()
    availability = scrapy.Field()
    number_of_review = scrapy.Field()
    """
