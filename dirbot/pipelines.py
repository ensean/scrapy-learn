from scrapy.exceptions import DropItem


class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    # put all words in lowercase

    def __init__(self):
       self.file = open('/tmp/dmoz.txt', 'wb')

    def process_item(self, item, spider):
       self.file.write(item['name'] + '\t'+ item['url'] + '\t' + item['desc']+'\n')
