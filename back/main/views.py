# from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import PopularPeople
from .models import InterestingFact

from .serializers import PeopleSerializers
from .serializers import FactsSerializers

class getPopularPeoples(APIView):
    def get(self, request):
        peoples = PopularPeople.objects.all()
        serializer_for_queryset = PeopleSerializers(
            instance=peoples,
            many=True
        )
        return Response(serializer_for_queryset.data)


class getInterestingFacts(APIView):
    def get(self, request):
        facts = InterestingFact.objects.all()
        serializer_for_queryset = FactsSerializers(
            instance=facts,
            many=True
        )
        return Response(serializer_for_queryset.data)
