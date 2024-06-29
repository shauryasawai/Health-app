from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .form import CallBookingForm


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
def medication_view(request):
    return render(request, 'base/medication.html')

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

@login_required
def chat_room(request):
    return render(request, 'base/room.html')
