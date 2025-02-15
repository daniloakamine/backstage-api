def calculate_difference_squares(number: int) -> int:
    sum_squares = 0
    square_sum = 0

    for i in range(1, number+1):
        sum_squares += i**2
        square_sum += i

    return (square_sum**2) - sum_squares


def is_pythagorean_triplet(a: int, b: int, c: int) -> bool:
    square_a = a**2
    square_b = b**2
    square_c = c**2
    return (square_a + square_b) == square_c


def calculate_product(a: int, b: int, c: int) -> int:
    return a * b * c
