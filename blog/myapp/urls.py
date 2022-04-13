from django.contrib import admin
from django.urls import path,include
from myapp import views


urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.user_register,name='register'),
    path('login/',views.user_login,name='login'),
    path('profile/',views.user_profile,name='profile'),
]
