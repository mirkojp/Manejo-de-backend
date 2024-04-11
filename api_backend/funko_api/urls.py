from django.urls import path
from funko_api import views


urlpatterns = [
    path("", views.index, name="index"),
]

