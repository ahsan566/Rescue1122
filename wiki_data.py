import scrapy

class WikiSpider(scrapy.Spider):
    name = 'wikispider'
    start_urls = ['https://en.wikipedia.org/wiki/Districts_of_Pakistan']

    custom_settings = {
        # specifies exported fields and order
        'FEED_EXPORT_FIELDS': ['district','area','population','density'],
    }

    def parse(self, response):
        table = response.xpath('//*[@id="mw-content-text"]//table[8]//tr')

        for row in table:
            yield {
                'district': row.xpath('normalize-space(td[2]//text())').extract_first(),
                'area': row.xpath('normalize-space(td[4]//text())').extract_first(),
                'population': row.xpath('normalize-space(td[5]//text())').extract_first(),
                'density': row.xpath('normalize-space(td[6]//text())').extract_first()
            }
