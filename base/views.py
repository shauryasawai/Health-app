from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .form import CallBookingForm
from django.shortcuts import render
from django.http import JsonResponse
import openai
from django.conf import settings
import openai
from django.conf import settings
from .form import ChatForm

def chat_view(request):
    response_text = ""
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            openai.api_key = settings.OPENAI_API_KEY
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": message}],
                max_tokens=150
            )
            response_text = response['choices'][0]['message']['content'].strip()
    else:
        form = ChatForm()

    return render(request, 'base/chat.html', {'form': form, 'response_text': response_text})

# Create your views here.
from django.shortcuts import render
from .form import PredictionForm
from .utils import predict_blood_sugar

def predict_view(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            bmi = form.cleaned_data['bmi']
            blood_pressure = form.cleaned_data['blood_pressure']
            result = predict_blood_sugar(bmi, blood_pressure)
            return render(request, 'base/result.html', {'result': result})
    else:
        form = PredictionForm()
    return render(request, 'base/predict.html', {'form': form})


# Create your views here.


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('base/home.html')  
    else:
        form = AuthenticationForm()
    return render(request, 'base/login.html', {'form': form})


def chat_page_view(request):
    return render(request, 'base/chat.html')


@login_required
def home_view(request):
    return render(request, 'base/home.html')

@login_required
def fitness_view(request):
    return render(request, 'base/fitness.html')

@login_required
def health_view(request):
    return render(request, 'base/health.html')

@login_required
def medication(request):
    return render(request, 'base/medication.html')

@login_required
def nutrition_view(request):
    return render(request, 'base/nutrition.html')

@login_required
def book_call(request):
    if request.method == 'POST':
        form = CallBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CallBookingForm()
    return render(request, 'base/book_call.html', {'form': form})

def success(request):
    return HttpResponse("Your call has been successfully booked!")

def room(request, room_name):
    return render(request, 'base/room.html', {
        'room_name': room_name
    })
def index(request):
    return render(request, 'base/index.html')

from django.shortcuts import render, get_object_or_404
from .models import Quiz, Question, UserResponse

@login_required
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'base/quiz_list.html', {'quizzes': quizzes})

@login_required
def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    if request.method == 'POST':
        for question in quiz.questions.all():
            selected_option = request.POST.get(str(question.id))
            UserResponse.objects.create(
                user=request.user,
                question=question,
                selected_option=selected_option
            )
        return render(request, 'base/quiz_result.html', {'quiz': quiz})
    else:
        return render(request, 'base/take_quiz.html', {'quiz': quiz})

# predictor/views.py
# health_app/views.py
import os
import joblib
from django.shortcuts import render
from .form import MoodForm
from .models import UserInput

# Define the path to the directory where the model and vectorizer are stored
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'mood_model.pkl')
VECTORIZER_PATH = os.path.join(BASE_DIR, 'vectorizer.pkl')

# Check if the model and vectorizer files exist
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
if not os.path.exists(VECTORIZER_PATH):
    raise FileNotFoundError(f"Vectorizer file not found: {VECTORIZER_PATH}")

# Load the machine learning model and vectorizer
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

def predict_mood(text):
    X = vectorizer.transform([text])
    prediction = model.predict(X)
    return prediction[0]

def mood_predictor_view(request):
    if request.method == 'POST':
        form = MoodForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            mood = predict_mood(text)
            UserInput.objects.create(text=text, mood=mood)
            return render(request, 'base/mood_result.html', {'mood': mood})
    else:
        form = MoodForm()
    return render(request, 'base/mood_form.html', {'form': form})

@login_required
def predictor_view(request):
    return render(request, 'base/health_predictor.html')
