from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('1/', views.index, name='index'),
    path('2/', views.nong, name='nong'),
    path('mul/', views.mul, name='mul'),

]
