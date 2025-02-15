from django.db import models


class SquareCalculation(models.Model):
    input_number = models.PositiveIntegerField(unique=True)
    output_number = models.IntegerField()
    occurrences = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    last_request_at = models.DateTimeField(auto_now=True)


class TripletCalculation(models.Model):
    input_number_a = models.IntegerField()
    input_number_b = models.IntegerField()
    input_number_c = models.IntegerField()
    is_pythagorean = models.BooleanField()
    product = models.IntegerField()
    occurrences = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    last_request_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            "input_number_a", "input_number_b", "input_number_c"
        )
