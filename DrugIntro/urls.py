from django.urls import path
from DrugIntro import views

urlpatterns=[
    path('Druginfolist/', views.Druginfolist, name='Druginfolist'),  # 這裡的name會對應到html跳轉網址的部分
    path('Druginfoview/', views.Druginfoview, name='Druginfoview'),
]