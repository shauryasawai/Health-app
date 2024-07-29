from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CallBooking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.date}"
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}"
    

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    option5 = models.CharField(max_length=200)
    option6 = models.CharField(max_length=200)
    option7 = models.CharField(max_length=200)
    option8 = models.CharField(max_length=200)
    correct_option = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


class UserInput(models.Model):
    text = models.TextField()
    mood = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
