from django.urls import path
from rest_framework import routers

from main.views import number_calculation_view


urlpatterns = [
    path('difference', number_calculation_view),
]
