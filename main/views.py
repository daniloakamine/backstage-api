from django.utils import timezone

from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from main.services import calculate_difference_squares


class NumberRequestSerializer(serializers.Serializer):
    n = serializers.IntegerField(min_value=1, max_value=100)


@api_view(["GET"])
def number_calculation_view(request: Request) -> Response:
    serializer = NumberRequestSerializer(data=request.query_params)
    serializer.is_valid(raise_exception=True)

    number_param = serializer.validated_data["n"]
    difference_squares = calculate_difference_squares(number_param)

    return Response(
        {
            "datetime": timezone.now(),
            "value": difference_squares,
            "number": number_param,
            "occurrences": None,
            "last_datetime": None,
        }
    )
