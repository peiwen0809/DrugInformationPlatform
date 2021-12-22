"""DrugInformationPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from DrugIntro.controller import DrugIntroViewSet
from DrugSearch.controller import DrugSearchViewSet
from SearchManage.controller import SearchManageViewSet
from django.conf.urls import url
from django.urls import path, include
from DrugInformationPlatform.adapter import *
from login.controller import AdminViewSet
from BaseTableSearch.controller import BaseTableSearchViewSet

router = DefaultRouter()
router.register(r'DrugIntro', DrugIntroViewSet, basename='common')
router.register(r'DrugSearch', DrugSearchViewSet, basename='common')
router.register(r'login', AdminViewSet, basename='common')
router.register(r'BaseTableSearch', BaseTableSearchViewSet, basename='common')
router.register(r'SearchManage', SearchManageViewSet, basename='common')

urlpatterns = [
    path('admin/', admin.site.urls),
    # 首頁
    path('', index, name='frontpage'),  # 這裡的name會對應到html跳轉網址的部分
    url(r'^DIP/', include(router.urls)),  # DIP：Drug Information Platform
    path('news/',include('DrugNews.urls')),
    path('Searchview/',include('DrugSearch.urls')),
    path('',include('DrugIntro.urls')),
    path('login/',include('login.urls')),
    path('',include('SearchManage.urls')),
]
