# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from .serializers import MsgSerializer
from . import models
from datetime import datetime
from rest_framework import status

from rest_framework import permissions
from rest_framework.decorators import permission_classes


class IsRecipient(permissions.BasePermission):
    """
    Permission to check if a user is a recipient
    """
    # def has_permission(self, request, view):
    #     return True

    def has_object_permission(self, request, view, obj):
        if obj.recipient == request.user:
            return True
        return False

class MsgViewSet(viewsets.ModelViewSet):
    # TODO: set serializer for Reciepient and Sender
    serializer_class = MsgSerializer

    @detail_route(methods=['patch'], permission_classes=[IsRecipient])
    def set_read(self, request, pk=None):
        msg = self.get_object()
        self.serializer_class = MsgSerializer

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

    @list_route(methods=['get'])
    def inbox(self, request):
        inbox = models.Msg.objects.all().filter(recipient=request.user)

        page = self.paginate_queryset(inbox)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(inbox, many=True)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def sent(self, request):
        # TODO: filter queryset correctly
        sent = models.Msg.objects.all().filter(sender=request.user)

        page = self.paginate_queryset(sent)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(sent, many=True)
        return Response(serializer.data)

