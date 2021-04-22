#Serializers used to convert model to JSON format

from rest_framework import serializers
from .models import *

class CitizenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citizen
        fields = '__all__' #Return all the fields

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__' #Return all the fields

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__' #Return all the fields

class ComplaintTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplaintTrack
        fields = '__all__' #Return all the fields

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__' #Return all the fields

class RequestTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestTrack
        fields = '__all__' #Return all the fields

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__' #Return all the fields