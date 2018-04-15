from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path(r'bgconverter/?(index.htm)?l?', views.BGConverterView.as_view(), name='index'),
    path(r'bgconverter/admin/?', admin.site.urls),
]
