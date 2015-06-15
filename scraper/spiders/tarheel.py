import scrapy

from scraper.items import TrailItem

class TarheelTrailblazersSpider(scrapy.Spider):

    name = "tarheeltrailblazers"
    allowed_domains = ["tarheeltrailblazers.com"]
    start_urls = ["http://www.tarheeltrailblazers.com/"]

    def parse(self, response):

        pass
