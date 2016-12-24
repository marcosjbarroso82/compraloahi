from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny

from apps.ad.serializers import AdSerializer
from apps.ad.models import Ad
from apps.notification.models import Notification
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
import math
# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest, JsonResponse

from .models import Favorite



class FavoriteAdViewSet(viewsets.ModelViewSet):
    serializer_class= AdSerializer
    paginate_by = 100
    queryset = Ad.objects.all()

    def get_queryset(self):
        lat = self.request.GET.get('lat', None)
        lng = self.request.GET.get('lng', None)

        # TODO: mejorar query de avisos favoritos (usar manager favorites)
        results =  Ad.objects.filter(id__in=Favorite.objects.for_user(self.request.user, model=Ad).values_list('target_object_id'))
        result = results

        # Filter by distance
        if lat and lng:
            if results.count() > 0:
                for ad in results:
                    a = float(ad.locations.first().lat) - float(lat)
                    b = float(ad.locations.first().lng) - float(lng)
                    dist = math.sqrt(math.pow(a,2)) + math.pow(b,2)
                    if dist > 0.085:
                        result = result.exclude(pk=ad.pk)
        return result

    def create(self, request, *args, **kwargs):
        if request.data.get('target_object_id'):
            ad_id = request.data.get('target_object_id')
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
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class HasFavoriteNearApiView(APIView):
    serializer_class = AdSerializer
    permission_classes = (AllowAny,)

    # def get_queryset(self):
    #     return Ad.objects.filter(id__in=Favorite.objects.for_user(self.request.user, model=Ad).values_list('target_object_id'))

    def post(self, request, *args, **kwargs):
        # = request.data.get('token')
        user = User.objects.get(auth_token=request.data.get('token'))
        if request.data.get('location'):
            loc_data = request.data.get('location')
            ads = Ad.objects.filter(id__in=Favorite.objects.for_user(user.id, model=Ad).values_list('target_object_id'))
            if ads.count() > 0:
                for ad in ads:
                    a = float(ad.locations.first().lat) - float(loc_data['latitude'])
                    b = float(ad.locations.first().lng) - float(loc_data['longitude'])
                    dist = math.sqrt(math.pow(a,2)) + math.pow(b,2)
                    if dist < 0.05:
                        Notification(receiver=user, type='prox', message="Estas cerca de avisos de tu interes", extras={'location': loc_data }).save()
                        return Response({"message": "Hay notificaciones"})

        return Response({"message": "No hay nada"})






@login_required
def add_or_remove(request):

    if not request.is_ajax():
        return HttpResponseNotAllowed()

    user = request.user

    try:
        app_model = request.POST["target_model"]
        obj_id = int(request.POST["target_object_id"])
    except (KeyError, ValueError):
        return HttpResponseBadRequest()

    fav = Favorite.objects.get_favorite(user, obj_id, model=app_model)

    if fav is None:
        Favorite.objects.create(user, obj_id, app_model)
        status = 'added'
    else:
        fav.delete()
        status = 'deleted'

    response = {
        'status': status,
        'fav_count': Favorite.objects.for_object(obj_id, app_model).count()
    }

    return JsonResponse(response)


@login_required
def remove(request):

    if not request.is_ajax():
        return HttpResponseNotAllowed()

    user = request.user

    try:
        app_model = request.POST["target_model"]
        obj_id = int(request.POST["target_object_id"])
    except (KeyError, ValueError):
        return HttpResponseBadRequest()

    Favorite.objects.get_favorite(user, obj_id, model=app_model).delete()
    status = 'deleted'

    response = {
        'status': status,
        }

    return JsonResponse(response)
