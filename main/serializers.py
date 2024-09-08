from rest_framework import serializers
from . import models


class ServicePartialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = ('id', 'name', 'get_image', 'description',)

class ServiceSerializer(serializers.ModelSerializer):
    service = ServicePartialSerializer(read_only=True)

    class Meta:
        model = models.Service
        fields = ('id', 'name', 'service', 'description', 'get_image',)


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = ('id', 'name', 'get_icon',)


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Banner
        fields = ('id', 'name', 'description', 'get_image',)
