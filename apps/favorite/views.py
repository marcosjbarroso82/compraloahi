from apps.ad.serializers import AdSerializer
from favit.models import Favorite
from apps.ad.models import Ad
from rest_framework import viewsets, status
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


