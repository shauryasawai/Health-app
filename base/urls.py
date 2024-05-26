from django.urls import path
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[
  path('', auth_views.LoginView.as_view(template_name='base/login.html'), name='login'),
  path('accounts/profile/', views.home_view , name='Health'),



]