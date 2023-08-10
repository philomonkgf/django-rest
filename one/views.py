from re import search
from django.shortcuts import render
from.serializers import Taskserializers
from.models import Task


from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.throttling import ScopedRateThrottle

# Create your views here.


class index(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = Taskserializers
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['taskname',]
    search_fields = ['taskname']
    ordering_fields = ['name','id']
    ordering = ['id']
    authentication_class = [BaseAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'user'
    # throttle_scope = 'anon'