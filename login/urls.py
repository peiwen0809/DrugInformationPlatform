from django.urls import path
from login import views

from . import controller

# app_name = 'login'
urlpatterns = [
    # ex: /login/index/
    # path('index/', views.index, name='index'),
    # path('', controller.AdminViewSet.login, name='login'),
    path('', views.login, name='login'),
    # ex: /polls/5/
    # the 'name' value as called by the {% url %} template tag
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
