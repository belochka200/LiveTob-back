from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *


def get_sights_by_category(cat):
    category = get_object_or_404(Category, category_name=cat)
    sights = Sight.objects.filter(category=category)
    return sights


def get_categories():
    return Category.objects.all()

class getSights(APIView):
    def get(self, request):
        count = int(request.GET.get("count", 0))
        category = request.GET.get("category", None)
        sight = request.GET.get("sight", None)
        if sight is None:
            if count == 0:
                if category:
                    serializer_for_queryset = SightSerializer(
                        instance=get_sights_by_category(category),
                        many=True
                    )
                else:
                    sights = Sight.objects.all()
                    serializer_for_queryset = SightSerializer(
                        instance=sights,
                        many=True
                    )
            else:
                if category:
                    serializer_for_queryset = SightSerializer(
                        instance=get_sights_by_category(category),
                        many=True
                    )
                else:
                    sights = Sight.objects.order_by('?')[:count]
                    serializer_for_queryset = SightSerializer(
                        instance=sights,
                        many=True
                    )
        else:
            sight = get_object_or_404(Sight, slug=sight)
            serializer_for_queryset = SightSerializer(
                instance=sight
            )
        return Response(serializer_for_queryset.data)


class getCategory(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer_for_queryset = CategorySerializer(
            instance=category,
            many=True
        )
        return Response(serializer_for_queryset.data)