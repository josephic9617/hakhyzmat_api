from django.db import models
from django.conf import settings


class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name="Service name")
    service = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="Service", related_name="services", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='services/', null=True, blank=True)

    def get_image(self):
        if self.image:
            return settings.API_URL + self.image.url
        else:
            return ''

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255, verbose_name='Brand')
    icon = models.ImageField(upload_to='brand_icons/')

    def get_icon(self):
        if self.icon:
            return settings.API_URL + self.icon.url
        else:
            return ''

    def __str__(self):
        return self.name

class Banner(models.Model):
    name = models.CharField(max_length=255, verbose_name='Banner')
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='banners/')

    def get_image(self):
        if self.image:
            return settings.API_URL + self.image.url
        else:
            return ''

    def __str__(self):
        return self.name 