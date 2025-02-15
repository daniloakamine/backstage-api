from django.test import TestCase

from main.math_functions import (
    calculate_difference_squares,
    calculate_product,
    is_pythagorean_triplet,
)


class TestServices(TestCase):
    def test_square_calculation(self):
        assert calculate_difference_squares(1) == 0
        assert calculate_difference_squares(3) == 22
        assert calculate_difference_squares(10) == 2640
        assert calculate_difference_squares(25) == 100100
        assert calculate_difference_squares(50) == 1582700
        assert calculate_difference_squares(100) == 25164150

    def test_pythagorean_triplet(self):
        assert is_pythagorean_triplet(3, 4, 5) is True
        assert is_pythagorean_triplet(5, 12, 13) is True
        assert is_pythagorean_triplet(6, 8, 10) is True
        assert is_pythagorean_triplet(6, 9, 11) is False
        assert is_pythagorean_triplet(10, 13, 15) is False
        assert is_pythagorean_triplet(45, 45, 90) is False

    def test_product_calculation(self):
        assert calculate_product(3, 4, 5) == 60
        assert calculate_product(1, 5, 8) == 40
        assert calculate_product(2, 10, 15) == 300

