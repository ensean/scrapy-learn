from scrapy.spiders import Spider
from scrapy.selector import Selector

from dirbot.items import Website


class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        sites = sel.xpath('//div[@class="title-and-desc"]')
        items = []        
        for site in sites:
            item = Website()
            item['name'] = site.xpath('a/div[@class="site-title"]/text()').extract_first()
            item['url'] = site.xpath('a/@href').extract_first()
            item['desc'] = site.xpath('div[@class="site-descr "]/text()').extract_first()
            items.append(item)

        return items
