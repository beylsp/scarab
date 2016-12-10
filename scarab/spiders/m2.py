import calendar
import datetime as dt
import scrapy

BASE_URL = 'http://media.motorsportmagazine.com/archive'
START = 1950
END = dt.date.today().year + 1


class M2Spider(scrapy.Spider):
    name = 'm2'
    
    def start_requests(self):
        for year in range(START, END):
            for month in calendar.month_name[1:13]:
                url = '%s/%s-%s/full/1.jpg' % (BASE_URL, month.lower(), year)
                self.logger.info('Request for %s' % url)
                yield scrapy.Request(url, self.parse)

    def parse(self, response):
        self.logger.info('Response from %s' % response.url)