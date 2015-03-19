from apps.ad.serializers import AdSerializer
from favit.models import Favorite
from apps.ad.models import Ad
from rest_framework import viewsets


class FavoriteAdViewSet(viewsets.ModelViewSet):
    serializer_class= AdSerializer
    paginate_by = 10
    queryset = Ad.objects.all()

    def get_queryset(self):
            # TODO: mejorar query de avisos favoritos (usar manager favorites)
            return Ad.objects.filter(id__in=Favorite.objects.for_user(self.request.user, model=Ad).values_list('target_object_id'))