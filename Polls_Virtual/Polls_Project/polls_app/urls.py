from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('vote/', views.vote, name='vote'),
    path('floor/', views.floor, name='floor'),
    path('counter/', views.counter, name='counter'),
    path('ec_login/', views.ec_login, name='ec_login'),
    path('ec_admin_result/', views.ec_admin_result, name='ec_admin_result'),
    path('invalid/', views.invalid, name='invalid'),
    # path('counter/', views.counter, name='counter'),

]
