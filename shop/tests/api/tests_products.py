import pytest
from rest_framework.test import APIClient

from products.models import Product


@pytest.mark.django_db
class TestProductsAPI:
    def setup_method(self):
        self.client = APIClient()

    def test_my_function(self):
        response = self.client.get("/api/products/")
        assert response.status_code == 200
        assert len(response.json()) == 0

    def test_post_function(self):
        response = self.client.post("/api/products/", data={
            "title": 'test',
            "price": '100',
            "description": 'test@test.by',
            "image": '',
            "color": 'RED',
        }, follow=True)
        assert response.status_code == 201
        assert Product.objects.exists()

        response = self.client.get("/api/products/")
        assert response.status_code == 200
        assert len(response.json()) == 1

    def test_delete_product(self):
        product = Product.objects.create(title='test', price='100', description='test@test.by', image='', color='RED')

        response = self.client.get(f"/api/products/{product.id}", follow=True)
        assert response.status_code == 200
        assert response.json()["title"] == 'test'

        response = self.client.delete(f"/api/products/{product.id}/", follow=True)
        assert response.status_code == 204
        assert not Product.objects.exists()

