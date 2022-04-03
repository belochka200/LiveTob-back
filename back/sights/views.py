from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *
# Create your views here.
class getAllSights(APIView):
    def get(self, request):
        sights = Sight.objects.all()
        serializer_for_queryset = SightSerializer(
            instance=sights,
            many=True
        )
        return Response(serializer_for_queryset.data)
