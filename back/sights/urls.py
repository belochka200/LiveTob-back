from .views import *
from django.urls import path


urlpatterns = [
    path('allSights/', getAllSights.as_view()),
]