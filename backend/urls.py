from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='admin'),
    path('regist/', views.regist_create_view, name='regist'),
    path('runner/', views.runner_create_view, name='runner'),
    path('manager/', views.manager_create_view, name='manager'),
    path('team/', views.team_create_view, name='team'),
    path('solo_runner/', views.solo_runner_create_view, name='solo_runner'),
    path('driver/', views.driver_create_view, name='driver'),
    path('finish/', views.registerfinish, name='finish'),
    path('team_for_runner/', views.team_for_runner_create_view,
         name='team_for_runner')


]
