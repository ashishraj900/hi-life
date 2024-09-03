"""
URL configuration for hilife project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from members.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='index_page'),
    path('basic_details/', basic_details),
    path('add_user_info/', add_user_info, name='add_user_info'),
    path('get_user_info_flat_basis/', get_user_info_flat_basis, name='get_user_info_flat_basis'),
    path('get_user_info/', get_user_info, name='get_user_info')
]
