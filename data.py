import scrapy

class RescueSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['http://www.rescue.gov.pk/Performance.aspx']

    custom_settings = {
        # specifies exported fields and order
        'FEED_EXPORT_FIELDS':  ['District','Total Calls','Emergency Calls','Road Accidents','Medical',
                                'Fire','Building Collapse','Crime Incidents','Drowning','Explosion',
                                'Misc','Fake Calls','Patients Rescued'],
    }

    def parse(self, response):
        table = response.xpath('//*[@class="formBorder"]//table//tr')

        for row in table:

            yield {
                'District' : row.xpath('td[1]//text()').extract_first(),
                'Total Calls' : row.xpath('td[2]//text()').extract_first(),
                'Emergency Calls' : row.xpath('td[3]//text()').extract_first(),
                'Road Accidents' : row.xpath('td[4]//text()').extract_first(),
                'Medical' : row.xpath('td[5]//text()').extract_first(),
                'Fire' : row.xpath('td[6]//text()').extract_first(),
                'Building Collapse' : row.xpath('td[7]//text()').extract_first(),
                'Crime Incidents' : row.xpath('td[8]//text()').extract_first(),
                'Drowning' : row.xpath('td[9]//text()').extract_first(),
                'Explosion' : row.xpath('td[10]//text()').extract_first(),
                'Misc' : row.xpath('td[11]//text()').extract_first(),
                'Fake Calls' : row.xpath('td[12]//text()').extract_first(),
                'Patients Rescued' : row.xpath('td[13]//text()').extract_first()
            }
