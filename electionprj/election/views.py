from django.shortcuts import render

def home(request):
    return render(request, 'election/home.html')

def registration(request):
    print("Hello registration")
    return render(request, 'election/registration.html')
