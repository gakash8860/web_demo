"""wevb_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from  .import views
from django.conf import settings
from django.conf.urls.static import static
# from .views import RegisterAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('List/',views.ListApi.as_view()),
    path('Create/',views.CreateApi.as_view()),
    path('Retrive/<int:pk>/',views.Retriv.as_view()),
    path('Ret/<int:pk>/',views.Retriv.as_view()),
    # path('api/', RegisterAPI.as_view(), name='register'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
