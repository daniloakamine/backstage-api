from datetime import datetime
from typing import Tuple

from django.db.models import F

from main.models import SquareCalculation, TripletCalculation
from main.math_functions import (
    calculate_difference_squares,
    calculate_product,
    is_pythagorean_triplet,
)


class SquareService:
    def fetch_calculation(input_number: int) -> Tuple[SquareCalculation, datetime]:
        last_request_at = None
        db_instance = SquareCalculation.objects.filter(input_number=input_number).first()
        if db_instance:
            last_request_at = db_instance.last_request_at
            db_instance.occurrences = F("occurrences") + 1
            db_instance.save()
            db_instance.refresh_from_db()
        else:
            db_instance = SquareCalculation.objects.create(
                input_number=input_number,
                output_number=calculate_difference_squares(input_number),
                occurrences=1,
            )

        return (db_instance, last_request_at)


class TripletService:
    def fetch_calculation(
        input_number_a: int, input_number_b: int, input_number_c: int
    ) -> Tuple[TripletCalculation, datetime]:
        last_request_at = None
        db_instance = TripletCalculation.objects.filter(
            input_number_a=input_number_a,
            input_number_b=input_number_b,
            input_number_c=input_number_c,
        ).first()

        if db_instance:
            last_request_at = db_instance.last_request_at
            db_instance.occurrences = F("occurrences") + 1
            db_instance.save()
            db_instance.refresh_from_db()
        else:
            db_instance = TripletCalculation.objects.create(
                input_number_a=input_number_a,
                input_number_b=input_number_b,
                input_number_c=input_number_c,
                is_pythagorean=is_pythagorean_triplet(input_number_a, input_number_b, input_number_c),
                product=calculate_product(input_number_a, input_number_b, input_number_c),
                occurrences=1,
            )

        return (db_instance, last_request_at)
