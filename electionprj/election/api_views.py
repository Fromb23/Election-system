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
