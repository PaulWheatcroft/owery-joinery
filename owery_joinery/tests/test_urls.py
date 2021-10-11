from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import index
from products.views import all_products, filtered_products
from django.contrib import admin


class TestUrls(SimpleTestCase):
    """ Ensuring all pages and their views resolve """
    def test_home_page_is_resolved(self):
        """ testing index """
        url = reverse('home')
        self.assertEqual(resolve(url).func, index)

    def test_products_page_is_resolved(self):
        """ testing all products being resolved """
        url = reverse('products')
        self.assertEqual(resolve(url).func, all_products)

    def test_products_filtered_page_is_resolved(self):
        """ testing products fiiltered by category id 3 """
        url = reverse('filtered_products', args=1)
        self.assertEqual(resolve(url).func, filtered_products)
