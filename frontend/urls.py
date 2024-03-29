from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signin', views.signin, name='signin'),
    path('editme', views.editme, name='editme'),
    path('test', views.test, name='test'),
    path('regis', views.regis, name='regis'),
    path('live', views.live, name='live'),
    path('certificate', views.certificate, name='certificate'),
    path('competitions/', views.competition_result, name='competitions'),
    url(r'^postsign/', views.postsign),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^postsignup/', views.postsignup, name='postsignup'),
    url(r'^logout/', views.logout, name="log")
]
