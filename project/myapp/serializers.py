from rest_framework import serializers
from .models import Geolocation, CustomUser
class GeolocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocation
        fields = ["id", "name", "latitude", "longitude"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password'] 