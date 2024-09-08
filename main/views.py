from rest_framework import generics
from . import models
from . import serializers


class ServiceView(generics.ListAPIView):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer


class BrandView(generics.ListAPIView):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer


class BannerView(generics.ListAPIView):
    queryset = models.Banner.objects.all()
    serializer_class = serializers.BannerSerializer
