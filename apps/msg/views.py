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
from apps.ad.models import Ad
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q

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


import pdb
class MsgViewSet(viewsets.ModelViewSet):
    serializer_class = MsgSerializer
    paginate_by = 10

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs and isinstance(kwargs["data"], list):
            kwargs["many"] = True
        return super(MsgViewSet, self).get_serializer(*args, **kwargs)

    def get_queryset(self):
        return models.Msg.objects.all()

    def destroy(self, request, *args, **kwargs):
        return Response({"message": "DELETE method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @detail_route(methods=['patch'], permission_classes=[IsRecipient])
    def set_read(self, request, pk=None):
        msg = self.get_object()
        self.serializer_class = MsgSerializer
        msg.set_read(datetime.now()).save()

        serializer = self.get_serializer(msg)
        return Response(serializer.data)

    def perform_create(self, serializer):
        # TODO: what if ad doesn't exists, how to handle exception ? How to make it generic for any model?
        recipient = Ad.objects.get(pk=serializer.validated_data['object_id']).author
        serializer.save(sender=self.request.user, recipient=recipient)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @detail_route(methods=['get'])
    def thread(self, request, pk):
        # TODO: Replace this with a custom object manager in the model
        msgs = models.Msg.objects.all().filter(Q(thread=pk) | Q(pk=pk))
        serializer = self.get_serializer(msgs, many=True)
        return Response(serializer.data)

    @list_route(methods=['put', 'patch'])
    def bulk(self, request):
        try:
            for msg_data in self.request.data:
                msg = models.Msg.objects.get(pk=msg_data['id'])
                serializer = self.get_serializer(msg, data=msg_data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
        except:
            return Response({'message': 'unexpected error'}, status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'success'}, status.HTTP_200_OK)

    @list_route(methods=['get'])
    def inbox(self, request):
        inbox = models.Msg.objects.all().filter(recipient=request.user, recipient_deleted_at__isnull=True)

        page = self.paginate_queryset(inbox)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(inbox, many=True)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def trash(self, request):
        # TODO: a better way for this queryset? maybe a custom object manager for Msg model
        trash = models.Msg.objects.all().filter(recipient=request.user, recipient_deleted_at__isnull=False)

        page = self.paginate_queryset(trash)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(trash, many=True)
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

    def list(self, request, *args, **kwargs):
        # return self.inbox(request)
        return Response([])