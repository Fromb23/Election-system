from rest_framework import generics
from .models import County, Constituency, Ward, PollingStation
from .serializers import CountySerializer, ConstituencySerializer, WardSerializer, PollingStationSerializer


class CountyList(generics.ListCreateAPIView):
    queryset = County.objects.all()
    print(f"This is the qurySet: {queryset}")
    serializer_class = CountySerializer

class CountyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = County.objects.all()
    serializer_class = CountySerializer

    # a polling_station
    polling_station = PollingStation.objects.get(id=2)
    polling_seri = WardSerializer(instance=polling_station)
    print(f"this is ward data: {polling_seri.data}")
