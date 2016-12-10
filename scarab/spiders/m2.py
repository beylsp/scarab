import urlparse

from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor as sle


class M2Spider(CrawlSpider):
    name = 'm2'
    allowed_domains = ['motorsportmagazine.com']
    start_urls = [
        'http://www.motorsportmagazine.com/archive/issues/all'
    ]
    rules = [
        Rule(sle(allow=('/archive/issues/*')),
             callback='parse_0', follow=True),
        Rule(sle(allow=('/archive/issue/*')),
             callback='parse_1', follow=True),
             
    ]

    def parse_0(self, response):
        self.logger.info('Response from %s' % response.url)

    def parse_1(self, response):
        self.logger.info('Response from %s' % response.url)
