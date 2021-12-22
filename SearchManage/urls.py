from django.urls import path
from SearchManage import views

urlpatterns=[
    # 這裡的name會對應到html跳轉網址的部分
    path('Mgrsearchview/', views.Mgrsearchview, name='Mgrsearchview'),
    path('MgrsearchviewAddcase/', views.MgrsearchviewAddcase, name='MgrsearchviewAddcase'),
    path('MgrsearchviewUpdatecase/', views.MgrsearchviewUpdatecase, name='MgrsearchviewUpdatecase'),
]