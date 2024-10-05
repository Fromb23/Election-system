from django.shortcuts import render
from .forms import VoterForm

def home(request):
    return render(request, 'election/home.html')

def registration(request):
    print("Hello registration")
    if request.method == "POST":
        form = VoterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = VoterForm()

    return render(request, 'election/registration.html', {'form': form})
