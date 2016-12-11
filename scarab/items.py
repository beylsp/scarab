import scrapy

from scrapy.loader.processors import Join


class IssueItem(scrapy.Item):
    pubdate = scrapy.Field(output_processor=Join())
    image_urls = scrapy.Field()
    images = scrapy.Field()
