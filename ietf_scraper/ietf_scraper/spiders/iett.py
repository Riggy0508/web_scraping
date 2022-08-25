from turtle import title
import scrapy


class IettSpider(scrapy.Spider):
    name = 'iett'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['https://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        #title1=response.xpath('//span[@class="pre noprint docinfo"]/text()').get()
        return {
            'number':response.xpath('//span[@class="rfc-no"]/text()').get(),
            'heading':response.xpath('//span[@class="subheading"]/text()').getAll(),
            'date':response.xpath('//span[@class="date"]/text()').get(),
        }
