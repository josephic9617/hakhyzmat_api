from django.db import models
from django.conf import settings


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    company_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=255)
    is_root_parent = models.BooleanField(default=False)
    parent_service = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class ServiceData(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    parent_service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def get_image(self):
        if self.image:
            return settings.API_URL + self.image.url
        else:
            return ''

    def __str__(self):
        return self.name

class Brand(models.Model):
    brand_name = models.CharField(max_length=255, verbose_name='Brand name')
    brand_icon = models.ImageField(upload_to='brand_icons/')
    banner_image = models.ImageField(upload_to='banners/', null=True, blank=True)
    banner_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Banner name')
    banner_description = models.TextField(null=True, blank=True, verbose_name='Banner description')

    def get_brand_icon(self):
        if self.brand_icon:
            return settings.API_URL + self.brand_icon.url
        else:
            return ''

    def get_banner_image(self):
        if self.banner_image:
            return settings.API_URL + self.banner_image.url
        else:
            return ''

    def __str__(self):
        return self.brand_name