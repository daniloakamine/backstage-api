from django.test import TestCase
from rest_framework.test import APIClient

from main.services import SquareService, TripletService


class TestServices(TestCase):
    def test_square_service(self):
        db_instance, last_request_at = SquareService.fetch_calculation(10)

        assert db_instance.input_number == 10
        assert db_instance.output_number == 2640
        assert db_instance.occurrences == 1
        assert db_instance.last_request_at is not None
        assert last_request_at is None

        for i in range(2, 5):
            db_instance, last_request_at = SquareService.fetch_calculation(10)
            assert db_instance.occurrences == i
            assert db_instance.last_request_at is not None
            assert last_request_at is not None

    def test_triplet_service(self):
        numbers_params = [3,4,5]

        db_instance, last_request_at = TripletService.fetch_calculation(*numbers_params)

        assert db_instance.input_number_a == 3
        assert db_instance.input_number_b == 4
        assert db_instance.input_number_c == 5
        assert db_instance.is_pythagorean is True
        assert db_instance.product == 60
        assert db_instance.occurrences == 1
        assert db_instance.last_request_at is not None
        assert last_request_at is None

        for i in range(2, 5):
            db_instance, last_request_at = TripletService.fetch_calculation(*numbers_params)
            assert db_instance.occurrences == i
            assert db_instance.last_request_at is not None
            assert last_request_at is not None
