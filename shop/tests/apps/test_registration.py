import pytest

from django.contrib.auth.models import User
from django.test.client import Client


@pytest.mark.django_db
class TestIndex:
    def setup_method(self):
        self.client = Client()

    def test_my_function(self):
        response = self.client.get("/register/")
        assert response.status_code == 200

        response = self.client.post(
            "/register/",
            data={
                "first_name": "test",
                "last_name": "test",
                "email": "test@test.by",
                "username": "tester",
                "password": "test@test.by",
                "repeat_password": "test@test.by",
                "are_you_older_18": True,
            },
            follow=True,
        )
        assert response.status_code == 200
        assert User.objects.exists()

        response = self.client.post(
            "/login/",
            data={
                "username": "tester",
                "password": "test@test.by",
            },
            follow=True,
        )
        assert response.status_code == 200
        assert User.objects.exists()
