from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import index, about, contact
from admin_tools.views import get_orders, view_order_details
from cart.views import (view_cart, add_to_cart, amend_cart,
                        remove_product_from_cart)
from checkout.views import checkout, cache_checkout_data
from products.views import (all_products, add_product, edit_product,
                            delete_product, filtered_products, product_details)
from profiles.views import profile, view_order


class TestHomeUrls(SimpleTestCase):
    """
    Test home app urls
    """
    def test_home_url_is_resolved(self):
        """ testing index """
        url = reverse('home')
        self.assertEqual(resolve(url).func, index)

    def test_about_url_is_resolved(self):
        """ testing about """
        url = reverse('about')
        self.assertEqual(resolve(url).func, about)

    def test_contact_url_is_resolved(self):
        """ testing about """
        url = reverse('contact')
        self.assertEqual(resolve(url).func, contact)


class TestAdminToolsUrls(SimpleTestCase):
    """
    Test admin_tools app urls
    """
    def test_get_orders_url_is_resolved(self):
        """ testing get_all_orders """
        url = reverse('get_orders')
        self.assertEqual(resolve(url).func, get_orders)

    def test_view_order_details_url_is_resolved(self):
        """ testing view_order_details """
        order_number = '336132C5B1'
        url = reverse('view_order_details', args=[order_number])
        self.assertEqual(resolve(url).func, view_order_details)


class TestCartUrls(SimpleTestCase):
    """
    Test cart app urls
    """
    def test_view_cart_url_is_resolved(self):
        """ testing view_cart """
        url = reverse('view_cart')
        self.assertEqual(resolve(url).func, view_cart)

    def test_add_to_cart_url_is_resolved(self):
        """ testing add_to_cart """
        product_id = '3'
        url = reverse('add_to_cart', args=[product_id])
        self.assertEqual(resolve(url).func, add_to_cart)

    def test_amend_cart_url_is_resolved(self):
        """ testing amend_cart """
        product_id = '3'
        url = reverse('amend_cart', args=[product_id])
        self.assertEqual(resolve(url).func, amend_cart)

    def test_remove_product_from_cart_url_is_resolved(self):
        """ testing remove_product_from_cart """
        product_id = '3'
        url = reverse('remove_product_from_cart', args=[product_id])
        self.assertEqual(resolve(url).func, remove_product_from_cart)


class TestCheckoutUrls(SimpleTestCase):
    """
    Test checkout app urls
    """
    def test_checkout_url_is_resolved(self):
        """ testing checkout """
        url = reverse('checkout')
        self.assertEqual(resolve(url).func, checkout)

    def test_checkout_success_url_is_resolved(self):
        """ testing checkout_success """
        url = reverse('checkout_success')
        self.assertEqual(resolve(url).func, checkout)

    def test_cache_checkout_data_url_is_resolved(self):
        """ testing cache_checkout_data """
        url = reverse('cache_checkout_data')
        self.assertEqual(resolve(url).func, cache_checkout_data)


class TestProductsUrls(SimpleTestCase):
    """
    Test products app urls
    """
    def test_products_url_is_resolved(self):
        """ testing all_products """
        url = reverse('products')
        self.assertEqual(resolve(url).func, all_products)

    def test_add_products_url_is_resolved(self):
        """ testing add_products """
        url = reverse('add_product')
        self.assertEqual(resolve(url).func, add_product)

    def test_edit_product_url_is_resolved(self):
        """ testing edit_product """
        product_id = '3'
        url = reverse('edit_product', args=[product_id])
        self.assertEqual(resolve(url).func, edit_product)

    def test_delete_product_url_is_resolved(self):
        """ testing delete_product """
        product_id = '3'
        url = reverse('delete_product', args=[product_id])
        self.assertEqual(resolve(url).func, delete_product)

    def test_filtered_products_url_is_resolved(self):
        """ testing filtered_products """
        category_id = '2'
        url = reverse('filtered_products', args=[category_id])
        self.assertEqual(resolve(url).func, filtered_products)

    def test_product_details_url_is_resolved(self):
        """ testing product_details """
        product_id = '3'
        url = reverse('product_details', args=[product_id])
        self.assertEqual(resolve(url).func, product_details)


class TestProfilesUrls(SimpleTestCase):
    """
    Test profiles app urls
    """
    def test_profile_url_is_resolved(self):
        """ testing checkout """
        url = reverse('profile')
        self.assertEqual(resolve(url).func, profile)

    def test_view_order_url_is_resolved(self):
        """ testing view_order """
        order_number = '336132C5B1'
        url = reverse('view_order', args=[order_number])
        self.assertEqual(resolve(url).func, view_order)
