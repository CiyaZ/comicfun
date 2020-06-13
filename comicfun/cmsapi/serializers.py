from rest_framework import serializers
from comicfun.models import *


class ConfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conf
        fields = '__all__'


class ContentTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentTag
        fields = '__all__'
