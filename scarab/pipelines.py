import scrapy.pipelines.images as spi

from scarab.utils import url_to_path
from scrapy.http import Request


class ImagesPipeline(spi.ImagesPipeline):
    def get_media_requests(self, item, info):
        self.pubdate = item['pubdate']
        return [Request(x) for x in item.get(self.images_urls_field, [])]

    def file_path(self, request, response=None, info=None):
        return url_to_path(request.url, self.pubdate)
