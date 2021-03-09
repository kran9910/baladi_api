from django.shortcuts import render
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet

from .models import *
from .serializers import *
from django.shortcuts import render,HttpResponseRedirect,Http404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def CitizensView(request):
    if request.method == 'GET':
        items = Citizen.objects.all()
        serializer = CitizenSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CitizenSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def CitizenView(request, citizen_id):
    try:
        item = Citizen.objects.get(id=citizen_id)
    except Citizen.DoesNotExist:
        raise Http404('Not found')

    if request.method == 'GET':
        serializer = CitizenSerializer(item)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CitizenSerializer(item, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    if request.method == "DELETE":
        item.delete()
        return HttpResponse(status=204)

