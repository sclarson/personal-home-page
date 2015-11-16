from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from grok.views import home_page

class HomePageTest(TestCase):
	
	def test_root_url_resolves_to_grok_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_contains_php_title(self):
		request = HttpRequest()
		response = home_page(request)
		self.assertIn(b'<title>Personal Home Page</title>', response.content)

	

