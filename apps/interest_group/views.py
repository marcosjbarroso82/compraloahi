from django.shortcuts import render
from rest_framework import viewsets
from .models import InterestGroup, Post
from .serializers import InterestGroupSerializer, PostSerializer
from django.views.generic import DetailView
from rest_framework.decorators import list_route, detail_route



class InterestGroupViewSet(viewsets.ModelViewSet):
    paginate_by = 100
    queryset = InterestGroup.objects.exclude(slug='public')
    serializer_class = InterestGroupSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(members=self.request.user.profile)



class PostViewSet(viewsets.ModelViewSet):
    paginate_by = 100
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class InterestGroupDetail(DetailView):
    template_name = "interest_group/details.html"
    model = InterestGroup
    context_object_name = 'group'
