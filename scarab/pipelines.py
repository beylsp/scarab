import glob
import os
import scrapy.pipelines.images as spi

from PIL import Image
from scarab.utils import url_to_path
from scrapy.http import Request
from scrapy.exceptions import DropItem


class ImagesPipeline(spi.ImagesPipeline):
    def get_media_requests(self, item, info):
        return [Request(x) for x in item.get(self.images_urls_field, [])]

    def file_path(self, request, response=None, info=None):
        try:
            return url_to_path(request.url)
        except ValueError:
            raise DropItem('Stop ImagesPipeline for %s' % request.url)


class PdfPipeline(object):
    def __init__(self, images_store):
        self.images_store = images_store

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            crawler.settings.get('IMAGES_STORE')
        )

    def process_item(self, item, spider):
        def process_pdf(pubdate):
            if not pubdate:
                raise ValueError('Invalid pubdate')
            m, y = pubdate.split('-')
            for im in glob.glob(os.path.join(self.images_store, y, m, '*.jpg')):
                spider.logger.info('Process pdf for %s' % im)
                n, _ = os.path.splitext(im)
                try:
                    image = Image.open(im).save('%s.pdf' % n)
                except Exception, err:
                    raise ValueError('Error converting %s: %s' % (im, err))

        # at least one image got updated, process all pdf again
        if item.get('images'):
            try:
                process_pdf(item.get('pubdate'))
            except Exception, err:
                raise DropItem('Stop PdfPipeline: %s' %  err)
        return item
