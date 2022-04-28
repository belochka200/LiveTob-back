from .views import *
from django.urls import path


urlpatterns = [
    path('sights/', getSights.as_view()),
    path('allCategories/', getCategory.as_view())
]