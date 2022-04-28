from rest_framework import serializers
from .models import Sight
from .models import Category


class CategorySerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    category_name = serializers.CharField(max_length=255)
    slug = serializers.SlugField()


class SightSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    category = serializers.CharField()
    views = serializers.IntegerField()
    full_text = serializers.CharField()
    price = serializers.CharField(max_length=255)
    adress = serializers.CharField(max_length=255)
    schedule = serializers.CharField(max_length=255)
    number = serializers.CharField(max_length=255)
    site = serializers.CharField(max_length=255)
    image = serializers.ImageField()