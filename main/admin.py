from django.contrib import admin

from main.models import SquareCalculation, TripletCalculation


@admin.register(SquareCalculation)
class SquareCalculationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "input_number",
        "output_number",
        "occurrences",
        "last_request_at",
    ]
    readonly_fields = ["last_request_at", "created_at"]


@admin.register(TripletCalculation)
class TripletCalculationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "input_number_a",
        "input_number_b",
        "input_number_c",
        "is_pythagorean",
        "product",
        "occurrences",
        "last_request_at",
    ]
    readonly_fields = ["last_request_at", "created_at"]
