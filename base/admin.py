from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Quiz, Question, UserResponse

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(UserResponse)
