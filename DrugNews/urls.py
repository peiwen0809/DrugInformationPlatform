from django.urls import path
from DrugNews import controller, views

urlpatterns=[
    # path('',views.index,name='index'),
    # path("test/",views.test,name='test'),
    # path("hello",views.hello),
    # path("addnews/",views.get_news),
    path("api/",controller.newsapi),
    path('api/<int:pk>',controller.newsid),
    path('Mgrnewsview/', views.Mgrnewsview, name='Mgrnewsview'),
    path('Newsview/', views.Newsview, name='Newsview'),
]