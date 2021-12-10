from django.urls import path
from DrugNews import views as dv
from rest_framework.urlpatterns import format_suffix_patterns
from DrugNews import views

from . import views
urlpatterns=[
    # path('',views.index,name='index'),
    # path("test/",views.test,name='test'),
    # path("hello",views.hello),
    # path("addnews/",views.get_news),
    path("api/",views.newsapi),
    path('api/<int:pk>',views.newsid),
    path('Mgrnewsview/', views.Mgrnewsview, name='Mgrnewsview'),
    path('Newsview/', views.Newsview, name='Newsview'),
]