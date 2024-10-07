from psycopg2 import IntegrityError
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import VoterForm

def home(request):
    return render(request, 'election/home.html')

def registration(request):
    print("Hello registration")
    if request.method == "POST":
        form = VoterForm(request.POST)
        if form.is_valid():
            form.save()
            print("form saved")
            return redirect('voter_login')
    else:
        form = VoterForm()

    return render(request, 'election/registration.html', {'form': form})

def voter_login(request):
    return render(request, 'election/voter_login.html')
