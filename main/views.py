from django.utils import timezone
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from main.services import SquareService, TripletService


class SquareRequestSerializer(serializers.Serializer):
    n = serializers.IntegerField(min_value=1, max_value=100)


@api_view(["GET"])
def square_view(request: Request) -> Response:
    serializer = SquareRequestSerializer(data=request.query_params)
    serializer.is_valid(raise_exception=True)
    number_param = serializer.validated_data["n"]

    db_instance, last_request_at = SquareService.fetch_calculation(number_param)

    return Response(
        {
            "datetime": timezone.now(),
            "value": db_instance.output_number,
            "number": number_param,
            "occurrences": db_instance.occurrences,
            "last_datetime": last_request_at,
        }
    )


class TripletRequestSerializer(serializers.Serializer):
    a = serializers.IntegerField()
    b = serializers.IntegerField()
    c = serializers.IntegerField(max_value=1000)


@api_view(["GET"])
def triplet_view(request: Request) -> Response:
    serializer = TripletRequestSerializer(data=request.query_params)
    serializer.is_valid(raise_exception=True)
    numbers_param = [
        serializer.validated_data["a"],
        serializer.validated_data["b"],
        serializer.validated_data["c"],
    ]

    db_instance, last_request_at = TripletService.fetch_calculation(*numbers_param)

    return Response(
        {
            "datetime": timezone.now(),
            "is_pythagorean": db_instance.is_pythagorean,
            "product": db_instance.product,
            "numbers": numbers_param,
            "occurrences": db_instance.occurrences,
            "last_datetime": last_request_at,
        }
    )
