from django.test import TestCase

from main.services import calculate_difference_squares


class TestServices(TestCase):
    def test_square_calculation(self):
        assert calculate_difference_squares(1) == 0
        assert calculate_difference_squares(3) == 22
        assert calculate_difference_squares(10) == 2640
        assert calculate_difference_squares(25) == 100100
        assert calculate_difference_squares(50) == 1582700
        assert calculate_difference_squares(100) == 25164150

