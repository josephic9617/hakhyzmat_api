from django.urls import path
from . import views


urlpatterns = [
    path('services/', views.ServiceView.as_view()),
    path('services/<int:parent_id>/', views.ServiceDataByParentIDView.as_view()),
    path('brands/', views.BrandView.as_view()),
    path('banners/', views.BannerView.as_view()),
]