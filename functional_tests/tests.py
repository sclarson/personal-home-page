from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class BasicHomepageSetup(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_item_text_in_item_list(self, page_item_text):
        itemlist = self.browser.find_element_by_id('links')
        items = itemlist.find_elements_by_tag_name('li')
        self.assertTrue(
            any(item.text == page_item_text for item in items)
        )

    def add_item_to_item_list(self, forminput, item_text):
        forminput.send_keys(item_text)
        forminput.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_item_text_in_item_list(item_text)

    def test_django_works(self):
        self.browser.get(self.live_server_url)
        self.browser.implicitly_wait(1)
        self.assertIn('Personal Home Page', self.browser.title)

    def test_can_post_a_link(self):
        self.browser.get(self.live_server_url)
        forminput = self.browser.find_element_by_id('new_link')
        self.assertEqual(
            forminput.get_attribute('placeholder'),
            'Enter a link'
        )
        self.add_item_to_item_list(
            forminput, 'feed://www.pyladies.com/feed.xml')
        forminput = self.browser.find_element_by_id('new_link')
        self.add_item_to_item_list(forminput, 'http://pyvideo.org/video/rss')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
