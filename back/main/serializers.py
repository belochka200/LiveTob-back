from rest_framework import serializers
from .models import *


class PeopleSerializers(serializers.Serializer):
    pk = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    bored = serializers.DateField()
    died = serializers.DateField()
    image = serializers.ImageField()


class FactsSerializers(serializers.Serializer):
    pk = serializers.IntegerField()
    text = serializers.CharField(max_length=255)
