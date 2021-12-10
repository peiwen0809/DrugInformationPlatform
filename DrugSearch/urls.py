from django.urls import path
from DrugSearch import views

urlpatterns=[
    path('', views.searchView, name='Searchview'),  # 這裡的name會對應到html跳轉網址的部分
]