from django.test import TestCase
from rest_framework.test import APIClient


class TestSquareView(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_input_error(self):
        response = self.client.get("/api/difference")
        assert response.status_code == 400
        assert response.json() == {"n": ["This field is required."]}

        response = self.client.get("/api/difference?n=0")
        assert response.status_code == 400
        assert response.json() == {"n": ["Ensure this value is greater than or equal to 1."]}

        response = self.client.get("/api/difference?n=101")
        assert response.status_code == 400
        assert response.json() == {"n": ["Ensure this value is less than or equal to 100."]}

    def test_success(self):
        response = self.client.get("/api/difference?n=10")
        assert response.status_code == 200
        
        content = response.json()
        assert content["datetime"] is not None
        assert content["value"] == 2640
        assert content["number"] == 10
        assert content["occurrences"] == 1
        assert content["last_datetime"] is None

        for i in range(2, 5):
            response = self.client.get("/api/difference?n=10")
            assert response.status_code == 200
            
            content = response.json()
            assert content["datetime"] is not None
            assert content["value"] == 2640
            assert content["number"] == 10
            assert content["occurrences"] == i
            assert content["last_datetime"] is not None
