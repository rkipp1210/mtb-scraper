import scrapy

from scraper.items import TrailItem

class WWCSpider(scrapy.Spider):
    name = "wwc"
    allowed_domains = [ "usnwc.org" ]
    start_urls = [ "http://usnwc.org" ]

    def parse(self, response):

        item = TrailItem()
        item['name'] = "Whitewater Center"

        imageName = response.xpath("//div[contains(@class,'trails-current')]//img/@src").extract()[1]
        if 'trailsopen' in imageName:
            item['status'] = 0
        elif 'trailsclosed' in imageName:
            item['status'] = 1
        else:
            item['status'] = 2

        yield item
