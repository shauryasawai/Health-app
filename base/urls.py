from django.urls import path
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include


urlpatterns=[
  path('', auth_views.LoginView.as_view(template_name='base/login.html'), name='login'),
  path('accounts/profile/', views.home_view , name='Home'),
  path('fitness/', views.fitness_view , name='Fitness'),
  path('health/', views.health_view, name='Health'),
  path('medication/', views.medication_view, name='index'),
  path('nutrition/', views.nutrition_view, name='nutrition'),
  path('book_call/', views.book_call, name='book_call'),
  path('success/', views.success, name='success'),
  path('chat/', views.chat_view, name='chat'),
  path('predict/', views.predict_view, name='predict'),
  
]