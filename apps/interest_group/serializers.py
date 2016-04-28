from rest_framework import serializers
from .models import InterestGroup


class InterestGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = InterestGroup

