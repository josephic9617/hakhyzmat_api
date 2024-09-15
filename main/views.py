from rest_framework import generics
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response


class ContactCreateView(APIView):
    def post(self, request):
        serializer = serializers.ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ServiceView(generics.ListAPIView):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer


class ServiceDataByParentIDView(APIView):
    def get(self, request, parent_id):
        services = models.ServiceData.objects.filter(parent_service__id=parent_id)
        serializer = serializers.ServiceDataSerializer(services, many=True)
        return Response(serializer.data)


class BrandView(generics.ListAPIView):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer


class BannerView(generics.ListAPIView):
    queryset = models.Banner.objects.all()
    serializer_class = serializers.BannerSerializer
