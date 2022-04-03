from rest_framework import serializers
from .models import Sight
from .models import Category


class SightSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    slug = serializers.SlugRelatedField(slug_field="pk", queryset=Category.objects)
    views = serializers.IntegerField()
    full_text = serializers.CharField()
    price = serializers.IntegerField()
    adress = serializers.CharField(max_length=255)
    schedule = serializers.CharField(max_length=255)
    number = serializers.CharField(max_length=255)
    site = serializers.CharField(max_length=255)
    image = serializers.ImageField()