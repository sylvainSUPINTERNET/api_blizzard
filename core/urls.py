from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('logout', views.user_logout, name='logout'),
    path('login', views.user_login, name='login')
]