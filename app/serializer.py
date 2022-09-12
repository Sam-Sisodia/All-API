from dataclasses import field
from . models import *
from rest_framework import serializers

class productserializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"