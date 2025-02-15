from django.test import TestCase
from rest_framework.test import APIClient


class TestTripletView(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_input_error(self):
        response = self.client.get("/api/triplet")
        assert response.status_code == 400
        assert response.json() == {
            "a": ["This field is required."],
            "b": ["This field is required."],
            "c": ["This field is required."],
        }

        response = self.client.get("/api/triplet?a=2")
        assert response.status_code == 400
        assert response.json() == {
            "b": ["This field is required."],
            "c": ["This field is required."],
        }

        response = self.client.get("/api/triplet?a=2&b=5")
        assert response.status_code == 400
        assert response.json() == {"c": ["This field is required."]}

        response = self.client.get("/api/triplet?a=2&b=5&c=1001")
        assert response.status_code == 400
        assert response.json() == {"c": ["Ensure this value is less than or equal to 1000."]}

    def test_success(self):
        response = self.client.get("/api/triplet?a=3&b=4&c=5")
        assert response.status_code == 200
        
        content = response.json()
        assert content["datetime"] is not None
        assert content["is_pythagorean"] is True
        assert content["product"] == 60
        assert content["numbers"] == [3,4,5]
        assert content["occurrences"] == 1
        assert content["last_datetime"] is None

        for i in range(2, 5):
            response = self.client.get("/api/triplet?a=3&b=4&c=5")
            assert response.status_code == 200
            
            content = response.json()
            assert content["datetime"] is not None
            assert content["is_pythagorean"] is True
            assert content["product"] == 60
            assert content["numbers"] == [3,4,5]
            assert content["occurrences"] == i
            assert content["last_datetime"] is not None
