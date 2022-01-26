from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('polls/<int:question_id>/', views.detail, name='detail'),
    path('polls/results/<int:question_id>/', views.results, name='results'),
    path('polls/vote/<int:question_id>/', views.vote, name='vote'),
]
