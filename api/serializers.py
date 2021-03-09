#Serializers used to convert model to JSON format

from rest_framework import serializers
from .models import *

class CitizenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citizen
        fields = '__all__' #Return all the fields