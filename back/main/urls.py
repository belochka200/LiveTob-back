from .views import *
from django.urls import path


urlpatterns = [
    path('popularPeoples', getPopularPeoples.as_view()),
    path('interestingFacts', getInterestingFacts.as_view())
]