from selenium import webdriver
import unittest

class BasicHomepageSetup(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_django_works(self):
		self.browser.get('http://localhost:8000')
		self.browser.implicitly_wait(1)
		self.assertIn('Personal Home Page', self.browser.title)

if __name__ == '__main__':
	unittest.main(warnings='ignore')
