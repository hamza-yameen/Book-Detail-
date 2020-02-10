# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request
from scrapy.loader import ItemLoader
from ..items import ToscrapeeItem


def product_table(response, value):
    return response.xpath("//th[text()='" + value + "']/following-sibling::td/text()").extract_first()


class BookSpider(Spider):
    name = 'book'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        books = response.xpath("//h3/a/@href").extract()
        for bk in books:
            absolute_url = response.urljoin(bk)
            yield Request(absolute_url, callback=self.parse_book)

        nextpage_url = response.xpath("//a[text()='next']/@href").extract_first()
        absolute_nextpage_url = response.urljoin(nextpage_url)
        yield Request(absolute_nextpage_url)

    def parse_book(self, response):
        l = ItemLoader(item=ToscrapeeItem(), response=response)

        title = response.css('h1::text').extract_first()
        price = response.xpath("//p[@class='price_color']/text()").extract_first()

        img_url = response.xpath("//img/@src").extract_first()
        image_url = img_url.replace('../../', 'http://books.toscrape.com/')

        rat = response.xpath('//*[contains(@class, "star-rating")]/@class').extract_first()
        rating = rat.replace('star-rating ', '')

        paragraph = response.xpath("//div[@id='product_description']/following-sibling::p").extract()

        upc = product_table(response, 'UPC')
        product_type = product_table(response, 'Product Type')
        price_witout_tax = product_table(response, 'Price (excl. tax)')
        price_with_tax = product_table(response, 'Price (excl. tax)')
        tex = product_table(response, 'tax')
        availability = product_table(response, 'Availability')
        number_of_review = product_table(response, 'Number of reviews')

        l.add_value('title', title)
        l.add_value('price', price)
        l.add_value('image_urls', image_url)

        return l.load_item()

"""
        yield {
            'Title': title,
            'Price': price,
            "Image Source": image_url,
            'Rating': rating,
            'Description': paragraph,
            "UPC": upc,
            'Product Type': product_type,
            'Price Without Tax': price_witout_tax,
            'Price With Tax': price_with_tax,
            'Tax': tex,
            'Availability': availability,
            'Number of Review': number_of_review
        }
        """
