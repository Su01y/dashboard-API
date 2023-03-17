# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .models import Aspirant, Technologies
from .serializers import AspirantSerializer, TechnologiesSerializer


class AspirantListView(generics.ListAPIView):
    serializer_class = AspirantSerializer
    queryset = Aspirant.objects.all()
    # filter_backends = [DjangoFilterBackend]
    # filteset_fields = ['education', 'rang', 'gender', 'exp', 'age', 'technologies', 'gpa']


class TechnologiesListView(generics.ListAPIView):
    serializer_class = TechnologiesSerializer
    queryset = Technologies.objects.all()
