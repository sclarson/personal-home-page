from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from grok.views import home_page
from grok.models import LinkItem


class HomePageTest(TestCase):

    def test_root_url_resolves_to_grok_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_contains_php_title(self):
        request = HttpRequest()
        response = home_page(request)
        expected = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected)

    def test_home_page_can_save_a_link_when_posted(self):
        url = 'http://pyladies.com/feed.xml'
        response = self.client.post(
            '/grok/new',
            data={'new_link': url}
        )
        self.assertEqual(LinkItem.objects.count(), 1)
        new_link = LinkItem.objects.first()
        self.assertEqual(new_link.url, url)

    def test_home_page_displays_all_list_items(self):
        pyladies_url = 'feed://www.pyladies.com/feed.xml'
        requests_url = 'http://docs.python-requests.org/en/latest/'
        LinkItem.objects.create(url=pyladies_url)
        LinkItem.objects.create(url=requests_url)
        request = HttpRequest()
        response = home_page(request)
        self.assertIn(pyladies_url, response.content.decode())
        self.assertIn(requests_url, response.content.decode())

    def test_home_page_redirects_after_POST_request(self):
        url = 'http://docs.python-requests.org/en/latest/'
        response = self.client.post(
            '/grok/new',
            data={'new_link': url}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')


class LinkItemModelTest(TestCase):

    def test_saving_and_reading_linkitems(self):
        first_link = LinkItem()
        first_link.url = 'feed://www.pyladies.com/feed.xml'
        first_link.save()

        second_link = LinkItem()
        second_link.url = 'http://docs.python-requests.org/en/latest/'
        second_link.save()

        saved_links = LinkItem.objects.all()
        self.assertEqual(saved_links.count(), 2)
        first_saved_link = saved_links[0]
        self.assertEqual(first_saved_link.url,
                         'feed://www.pyladies.com/feed.xml')
        second_saved_link = saved_links[1]
        self.assertEqual(second_saved_link.url,
                         'http://docs.python-requests.org/en/latest/')
