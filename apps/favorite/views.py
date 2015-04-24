from rest_framework.authentication import TokenAuthentication
from apps.ad.serializers import AdSerializer
from favit.models import Favorite
from apps.ad.models import Ad
from apps.notification.models import Notification
from rest_framework import viewsets, status, generics
from rest_framework.response import Response


class FavoriteAdViewSet(viewsets.ModelViewSet):
    serializer_class= AdSerializer
    paginate_by = 10
    queryset = Ad.objects.all()

    def get_queryset(self):
            # TODO: mejorar query de avisos favoritos (usar manager favorites)
            return Ad.objects.filter(id__in=Favorite.objects.for_user(self.request.user, model=Ad).values_list('target_object_id'))

    def create(self, request, *args, **kwargs):
        if request.DATA.get('target_object_id'):
            ad_id = request.DATA.get('target_object_id')
            try:
                ad = Ad.objects.get(pk= ad_id)

                fav = Favorite.objects.get_favorite(request.user, ad_id, 'ad.Ad')

                if fav is None:
                    Favorite.objects.create(request.user, ad, 'ad.Ad')
                    action = 'added'
                else:
                    fav.delete()
                    action = 'deleted'

                message = "Success " + action + " favorite"
                return Response({"message": message}, status=status.HTTP_200_OK)
            except Ad.DoesNotExist:
                return Response({"message": "Error, the ad dont exists"}, status=status.HTTP_400_BAD_REQUEST)


import math
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

import ast
from rest_framework import authentication, permissions


from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from django.contrib.auth.models import User

import logging

logger = logging.getLogger('debug')
import json

class HasFavoriteNearApiView(APIView):
    serializer_class = AdSerializer
    authentication_classes = (authentication.TokenAuthentication,)

    def get_queryset(self):
        return Ad.objects.filter(id__in=Favorite.objects.for_user(self.request.user, model=Ad).values_list('target_object_id'))

    def post(self, request, *args, **kwargs):
        # = request.DATA.get('token')
        user = User.objects.get(auth_token=request.DATA.get('token'))
        if request.DATA.get('location'):
            loc_data = request.DATA.get('location')
            ads = Ad.objects.filter(id__in=Favorite.objects.for_user(user.id, model=Ad).values_list('target_object_id'))
            if ads.count() > 0:
                for ad in ads:
                    a = float(ad.locations.first().lat) - float(loc_data['latitude'])
                    b = float(ad.locations.first().lng) - float(loc_data['longitude'])
                    dist = math.sqrt(math.pow(a,2)) + math.pow(b,2)
                    if dist < 0.05:
                        Notification(receiver=user, type='prox', message="Avisos cerca", extras={'location': "hola" }).save()
                        return Response({"message": "Hay notificaciones"})

        return Response({"message": "No hay nada"})


# @api_view(['POST'])
# def hasFavoriteNear(request):
#
#     #return HttpResponse( "algo" )
#     request_data = {}
#
#     print(request.DATA)
#
#
#     request_data = request.DATA
#
#     print("DATOS DE USUARIO")
#     print(request.user)
#
#     if request_data.get('location'):
#
#         loc_data = request_data.get('location')
#         print(loc_data)
#         if Ad.objects.filter(id__in=Favorite.objects.for_user(request.user, model=Ad).values_list('target_object_id')).count() > 0:
#             print("ENTRO1")
#             for ad in Ad.objects.filter(id__in=Favorite.objects.for_user(request.user, model=Ad).values_list('target_object_id')):
#                 dist = math.sqrt(math.exp(ad.locations.first().lat - loc_data['latitude']) + math.exp(ad.locations.first().lng - loc_data['longitude']))
#                 print("DISTANCIA")
#                 print(dist)
#                 if dist < 0.01:
#                     Notification(receiver=request.user, type='near', message="Avisos cerca", extras={'location': loc_data }).save()
#                     return Response({"message": "Hay notificaciones"})
#
#     return Response({"message": "No hay nada"})
#
#
#
# class HasFavoriteNearApiView(generics.CreateAPIView):
#     serializer_class = AdSerializer
#
#     def get_queryset(self):
#         return Ad.objects.filter(id__in=Favorite.objects.for_user(self.request.user, model=Ad).values_list('target_object_id'))
#
#
#     def create(self, request, *args, **kwargs):
#         print(request.DATA)
#         if request.DATA.get('location'):
#             loc_data = request.DATA.get('location')
#             print(loc_data)
#             if Ad.objects.filter(id__in=Favorite.objects.for_user(self.request.user, model=Ad).values_list('target_object_id')).count() > 0:
#                 for ad in Ad.objects.filter(id__in=Favorite.objects.for_user(self.request.user, model=Ad).values_list('target_object_id')):
#                     dist = math.sqrt(math.exp(ad.locations.first().lat - loc_data['latitude']) + math.exp(ad.locations.first().lng - loc_data['longitude']))
#                     if dist < 0.01:
#                         Notification(receiver=request.user, type='near', message="Avisos cerca", extras={'location': loc_data }).save()
#                         return Response({"message": "Hay notificaciones"})
#
#
#         return Response({"message": "No hay nada"})
#


