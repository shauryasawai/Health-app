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
  path('book_call/', views.book_call, name='book_call'),
  path('success/', views.success, name='success'),
  path('room/', views.index, name='index'),
  path('<str:room_name>/', views.room, name='room'),
  path('chat/', views.chat_view, name='chat'),
  path('chat_page/', views.chat_page_view, name='chat_page'),
]