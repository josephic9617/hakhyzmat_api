from rest_framework import serializers
from . import models


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = ('id', 'name', 'email', 'company_name', 'phone_number', 'message',)

class ServiceSerializer(serializers.ModelSerializer):
    subservices = serializers.SerializerMethodField()

    class Meta:
        model = models.Service
        fields = ('id', 'name', 'subservices',)

    def get_subservices(self, instance):
        subservices = instance.service_set.all()
        serializer = ServiceSerializer(subservices, many=True)
        return serializer.data


class ServiceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceData
        fields = ('id', 'name', 'description', 'get_image',)


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = ('id', 'name', 'get_icon',)


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Banner
        fields = ('id', 'name', 'description', 'get_image',)
