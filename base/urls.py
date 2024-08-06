from django.urls import path
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import mood_predictor_view
from .views import predictor_view
from . import views
from .views import logout_view,about_us
from .views import custom_login
from .views import reset_password
from .views import CustomPasswordResetCompleteView



urlpatterns=[
  path('', views.login_view , name='login'),
  path('signup/', views.signup, name='signup'),
  path('accounts/profile/', views.home_view , name='Home'),
  path('fitness/', views.fitness_view , name='Fitness'),
  path('health/', views.health_view, name='Health'),
  path('medication/', views.medication, name='medication'),
  path('nutrition/', views.nutrition_view, name='nutrition'),
  path('book_call/', views.book_call, name='book_call'),
  path('success/', views.success, name='success'),
  path('predict/', views.predict_view, name='predict'),
  path('quizzes/', views.quiz_list, name='quiz_list'),
  path('quiz/<int:quiz_id>/', views.take_quiz, name='take_quiz'),
  path('mood/', mood_predictor_view, name='mood_predictor'),
  path('predictors/', predictor_view, name='predictor'),
  path('logout/', logout_view, name='logout'),
  path('custom_login/', custom_login, name='custom_login'),
  path('forgot-password/', views.forgot_password, name='forgot-password'),
  path('reset-password/',reset_password, name='reset-password'),
  path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
  path('logout/', logout_view, name='logout'),
]