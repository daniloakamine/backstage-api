from django.urls import path

from main.views import square_view, triplet_view


urlpatterns = [
    path("difference", square_view),
    path("triplet", triplet_view),
]
