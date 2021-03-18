from rest_framework import viewsets
from . import models
from . import serializers

class CitizenViewset(viewsets.ModelViewSet):
    queryset = models.Citizen.objects.all()
    serializer_class = serializers.CitizenSerializer