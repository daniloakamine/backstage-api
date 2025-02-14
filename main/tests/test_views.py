from django.test import TestCase
from rest_framework.test import APIClient


class TestViews(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_difference_api(self):
        response = self.client.get("/api/difference?n=10")
        assert response.status_code == 200
        
        content = response.json()
        assert content["value"] == 2640
