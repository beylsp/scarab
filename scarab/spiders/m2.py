import os
import urlparse

from scarab.items import IssueItem
from scrapy.loader import ItemLoader
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
        Rule(sle(allow=('/archive/issues/*'))),
        Rule(sle(allow=('/archive/issue/*')),
             callback='parse_1', follow=True),
    ]

    def parse_1(self, response):
        self.logger.info('Response from %s' % response.url)
        sil = ItemLoader(item=IssueItem(), response=response)
        image_urls = []

        urlp = urlparse.urlparse(response.url)
        pubdate = os.path.basename(urlp.path)
        sil.add_value('pubdate', pubdate)

        pages = response.xpath('//div[@id="carousel"]/a/span/text()').extract()
        image_urls.extend(
            ['http://media.motorsportmagazine.com/archive/%s/full/%s.jpg' % (
                pubdate, x) for x in pages])

        sil.add_value('image_urls', image_urls)
        return sil.load_item()
