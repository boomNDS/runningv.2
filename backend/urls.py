from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='admin'),
    path('regist/', views.regist_create_view, name='regist')
]
