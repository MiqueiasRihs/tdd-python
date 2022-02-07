from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        # resolve é uma funcao que Django utiliza internamente para resolver
        # URL's e descobrir para qual funcao de view eles devem ser mapeados.
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_corret_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('html>'))
