from psycopg2 import IntegrityError
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import VoterForm, FilterForm
from .models import PollingStation

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

def search_polling_stations(request):
    stations = PollingStation.objects.all()
    form = FilterForm(request.GET or None)

    # Filete based on selections
    if request.GET:
        if form.is_valid():
            county = form.cleaned_data.get('county')
            constituency = form.cleaned_data.get('constituency')
            ward = form.cleaned_data.get('ward')
            polling_station = form.cleaned_data.get('polling_station')

            print(f"Count is: {county}, Cosnt is: {constituency}, Ward is: {ward}, PollingStation is: {polling_station}")

            # Apply filter based on user selection
            if county:
                stations = stations.filter(ward__constituency__county=county)
            if constituency:
                stations = stations.filter(ward_constituency=constituency)
            if ward:
                stations = stations.filter(ward=ward)
            if polling_station:
                stations = stations.filter(id=polling_station.id)

    return render(request, 'election/search_polling_stations.html', {'form': form, 'stations': stations})
