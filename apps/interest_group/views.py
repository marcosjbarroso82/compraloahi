from django.shortcuts import render
from rest_framework import viewsets
from .models import InterestGroup
from .serializers import InterestGroupSerializer


class InterestGroupViewSet(viewsets.ModelViewSet):
    paginate_by = 100
    queryset = InterestGroup.objects.all()
    serializer_class = InterestGroupSerializer


