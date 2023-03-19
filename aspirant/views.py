# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Aspirant, Technologies
from .serializers import AspirantSerializer, TechnologiesSerializer


class AspirantListView(generics.ListAPIView):
    serializer_class = AspirantSerializer
    queryset = Aspirant.objects.all()


class FilterTechnologies(APIView):
    def post(self, request):
        field_value = request.data.get('technologies', ())
        aspirants = Aspirant.objects.filter(technologies__in=field_value)
        serializer = AspirantSerializer(aspirants, many=True)
        return Response(serializer.data)


class SelectedAspirents(APIView):
    def post(self, request):
        field_value = request.data.get('id', ())
        aspirants = Aspirant.objects.filter(id__in=field_value)
        serializer = AspirantSerializer(aspirants, many=True)
        return Response(serializer.data)


class TechnologiesListView(generics.ListAPIView):
    serializer_class = TechnologiesSerializer
    queryset = Technologies.objects.all()
