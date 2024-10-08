from rest_framework import serializers
from .models import County, Constituency, Ward, PollingStation

class PollingStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollingStation
        fields = ['id', 'name']

class WardSerializer(serializers.ModelSerializer):
    polling_stations = PollingStationSerializer(many=True, read_only=True)
    class Meta:
        model = Ward
        fields = ['id', 'name', 'polling_stations']

class ConstituencySerializer(serializers.ModelSerializer):
    wards = WardSerializer(many=True, read_only=True)
    class Meta:
        model = Constituency
        fields = ['id', 'name', 'wards']

class CountySerializer(serializers.ModelSerializer):
    constituencies = ConstituencySerializer(many=True, read_only=True)
    class Meta:
        model = County
        fields = ['id', 'name', 'constituencies']
