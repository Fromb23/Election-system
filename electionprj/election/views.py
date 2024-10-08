from psycopg2 import IntegrityError
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import VoterForm, FilterForm
from .models import PollingStation, Constituency, Ward, Voter

def home(request):
    return render(request, 'election/home.html')

def registration(request):
    print("Hello registration")
    if request.method == "POST":
        form = VoterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Voter.objects.filter(email=email).exists():
                print("Views: A user with similar email already exists")
                form.add_error('email', 'This email alredy exists')
                user_exists = True
            else:
                form.save_voter()
                print("form saved")
                return redirect('voter_login')
    else:
        form = VoterForm()

    return render(request, 'election/registration.html', {'form': form})


def voter_login(request):
    return render(request, 'election/voter_login.html')

def search_polling_stations(request):
    # stations = PollingStation.objects.all()
    form = FilterForm(request.GET or None)

    county = request.GET.get('county')
    constituency = request.GET.get('constituency')
    ward = request.GET.get('ward')
    polling_station = request.GET.get('polling_station')

    if county:
        form.fields['constituency'].queryset = Constituency.objects.filter(county=county)
        form.fields['county'].initial = county
    if constituency:
        form.fields['ward'].queryset = Ward.objects.filter(constituency=constituency)
    if ward:
        form.fields['polling_station'].queryset = PollingStation.objects.filter(ward=ward)

    polling_stations = PollingStation.objects.all()
    if polling_station:
        polling_stations = polling_stations.filter(id=polling_station)
    elif ward:
        polling_stations = polling_stations.filter(ward=ward)
    elif constituency:
        polling_stations = polling_stations.filter(ward__constituency=constituency)
    elif county:
        polling_stations = polling_stations.filter(ward__constituency__county=county)

    return render(request, 'election/search_polling_stations.html', {'form': form, 'polling_stations': polling_stations})
