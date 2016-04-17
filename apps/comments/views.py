import datetime

from django.db.models import F

from django_comments_xtd.models import XtdComment

from django_filters import FilterSet, MethodFilter

from rest_framework import viewsets, filters
from rest_framework.decorators import list_route

from apps.program.models import Episode

from .serializers import XtdCommentSerializer


class XtdCommentFilter(FilterSet):
    id_not = MethodFilter(action='filter_id')
    class Meta:
        model = XtdComment
        fields = ['object_pk', 'user', 'parent_id', 'id_not']

    def filter_id(self, queryset, value):
        return queryset.exclude(pk=value)


class ThreadedCommentViewSet(viewsets.ModelViewSet):
    queryset = XtdComment.objects.all()
    serializer_class = XtdCommentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = XtdCommentFilter

    def perform_create(self, serializer):
        content_object = Episode.objects.get(pk=self.request.data.get('object_pk', 0))
        if self.request.user.is_authenticated():
            serializer.save(user=self.request.user,
                            content_object=content_object,
                            submit_date=datetime.datetime.today(),
                            site_id=1)
        return super(ThreadedCommentViewSet, self).perform_create(serializer)

    @list_route(methods=['get'])
    def last(self, request, *args, **kwargs):
        self.queryset = self.get_queryset().filter(pk=F('parent_id'))
        return super(ThreadedCommentViewSet,self).list(request, *args, **kwargs)
