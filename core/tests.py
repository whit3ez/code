from django.test import TestCase
from django.urls import reverse
from core import factories


class ProductListViewTest(TestCase):
    def setUp(self):
        self.url = reverse('core:product_list')

    def test_product_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/product_list.html')

    def test_product_list_context(self):
        products = factories.ProductFactory.create_batch(3)
        response = self.client.get(self.url)
        self.assertEqual(list(response.context['products']), products)


class ProductDetailViewTest(TestCase):
    def setUp(self):
        self.product = factories.ProductFactory()
        self.url = reverse('core:product_detail', kwargs={'pk': self.product.pk})

    def test_product_detail_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/product_detail.html')

    def test_product_detail_context(self):
        response = self.client.get(self.url)
        self.assertEqual(response.context['product'], self.product)


class ClientListViewTest(TestCase):
    def setUp(self):
        self.url = reverse('core:client_list')

    def test_client_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/client_list.html')

    def test_client_list_context(self):
        clients = factories.ClientFactory.create_batch(3)
        response = self.client.get(self.url)
        self.assertEqual(list(response.context['clients']), clients)