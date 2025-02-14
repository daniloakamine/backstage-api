def calculate_difference_squares(number: int) -> int:
    sum_squares = 0
    square_sum = 0

    for i in range(1, number+1):
        sum_squares += i**2
        square_sum += i

    return (square_sum**2) - sum_squares
