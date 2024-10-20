from django.contrib import admin
from . import models


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'company_name',
        'phone_number',
        'message',
    )
    search_fields = (
        'id',
        'name',
        'email',
        'company_name',
        'phone_number',
        'message',
    )

admin.site.register(models.Contact, ContactAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'is_root_parent',
        'parent_service',
    )

admin.site.register(models.Service, ServiceAdmin)


class ServiceDataAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'parent_service',
        'get_image',
    )

admin.site.register(models.ServiceData, ServiceDataAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'brand_name',
        'get_brand_icon',
        'banner_name',
        'banner_description',
        'get_banner_image',
    )
admin.site.register(models.Brand, BrandAdmin)
