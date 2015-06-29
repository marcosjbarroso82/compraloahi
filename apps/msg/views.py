from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from .serializers import MsgSerializer, MsgSerializer2
from . import models
from datetime import datetime
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

class MsgViewSet(viewsets.ModelViewSet):

    serializer_class = MsgSerializer

    @detail_route(methods=['patch'])
    def set_read(self, request, pk=None):
        msg = self.get_object()
        # self.serializer_class = MsgSerializer2

        self.serializer_class = MsgSerializer
        # serializer = PasswordSerializer(data=request.data)

        serializer = self.get_serializer(data=request.data, partial=True)
        if serializer.is_valid():
            msg.set_read(datetime.now())
            msg.save()
            serializer = self.get_serializer(msg)
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return models.Msg.objects.all()


    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
#@detail_route(methods=['post'], permission_classes=[IsAdminOrIsSelf])

sdfk
sd
    @list_route(methods=['get'])
    def inbox(self, request):
        inbox = models.Msg.objects.all()

        page = self.paginate_queryset(inbox)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(inbox, many=True)
        return Response(serializer.data)

