
import scrapy

# status is either:
#	0 => closed
#	1 => open
#	2 => unknown

class TrailItem(scrapy.Item):
    name = scrapy.Field()
    status = scrapy.Field() 
