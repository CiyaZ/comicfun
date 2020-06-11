from rest_framework import serializers
from comicfun.models import *


class ConfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conf
        fields = '__all__'
