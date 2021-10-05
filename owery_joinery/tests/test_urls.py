from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import index
from django.contrib import admin


class TestUrls(SimpleTestCase):
    """ Ensuring all pages and their views resolve """
    def test_home_page_is_resolved(self):
        """ testing index.html """
        url = reverse('home')
        self.assertEqual(resolve(url).func, index)

