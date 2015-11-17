import unittest
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "personalhomepage.settings")
from grok.models import LinkItem

class LinkItemProcessorTests(unittest.TestCase):

    def test_processor_reads_urls(self):
       processor = LinkItemProcessor()
       info = processor.getqueuesize()


class LinkItemProcessor(object):

    def __init__(self):
        pass

    def getqueuesize(self):
        return LinkItem.objects.count()

    def processnext(self):
        link = LinkItem.objects.first()

    
if __name__ == '__main__':
    unittest.main()

