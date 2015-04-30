from rest_framework import status
from rest_framework.generics import UpdateAPIView, CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet

from push_notifications.models import GCMDevice

from .serializers import DeviceSerializer, NotificationSerializer, ConfigNotificationSerializer
from .models import Notification, ConfigNotification


class RegisterGCMNotification(CreateAPIView):
    serializer_class = DeviceSerializer

    def create(self, request, *args, **kwargs):
        try:
            device_id = int(str(request.DATA['device_id']), 16)
            gcm = GCMDevice.objects.get(user=request.user,
                                        #registration_id= request.DATA['registration_id'],
                                        device_id= device_id)
            gcm.active = True
            gcm.registration_id = request.DATA['registration_id']
            gcm.device_id = device_id
            gcm.save()
            return Response({"message": "Success registered notification"}, status=status.HTTP_200_OK)
        except GCMDevice.DoesNotExist:
            try:
                return super(RegisterGCMNotification, self).create(request, *args, **kwargs)
            except:
                return Response({"message": "Error registered notification"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message": "Error registered notification"}, status=status.HTTP_400_BAD_REQUEST)


class UnregisterGCMNotification(UpdateAPIView):
    serializer_class = DeviceSerializer

    def update(self, request, *args, **kwargs):
        if request.DATA.get('registration_id', '') != '':
            try:
                device_id = int(str(request.DATA['device_id']), 16)
                gcm = GCMDevice.objects.get(user=request.user,
                       #registration_id= request.DATA.get('registration_id'),
                       device_id= device_id)
                gcm.active = False
                gcm.save()
                return Response({"message": "Success! User unregistered to notification"}, status=status.HTTP_200_OK)
            except GCMDevice.DoesNotExist:
                return Response({'message': "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': "Field registration id is required."}, status=status.HTTP_400_BAD_REQUEST)



class NotificationRetrieveApiView(RetrieveAPIView):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk', '') != '':
            try:
                notification = Notification.objects.get(id=kwargs['pk'])
                notification.marked_read()
                return super(NotificationRetrieveApiView, self).retrieve(request, *args, **kwargs)
            except Notification.DoesNotExist:
                return Response({'message': 'Error!'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Need param id notification'}, status=status.HTTP_400_BAD_REQUEST)


class NotificationListApiView(ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(receiver= self.request.user)


class NotificationMarkBulkReadApiView(UpdateAPIView):
    serializer_class = NotificationSerializer

    def update(self, request, *args, **kwargs):
        notifications = request.DATA.get('notifications', [])
        if len(notifications) > 0:
            for notification in notifications:
                try:
                    Notification.objects.get(pk=notification['id']).marked_read()
                except:
                    pass
            return Response({'message': 'Success, notifications mark readed'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Error, need array to notifications'}, status=status.HTTP_400_BAD_REQUEST)


class ConfigNotificationModelViewSet(ModelViewSet):
    serializer_class = ConfigNotificationSerializer

    def get_object(self):
        return ConfigNotification.objects.get(user= self.request.user)

    def get_queryset(self):
        return ConfigNotification.objects.get(user= self.request.user)

    def update(self, request, *args, **kwargs):
        print(request.DATA)
        return super(ConfigNotificationModelViewSet, self).update(request, *args, **kwargs)