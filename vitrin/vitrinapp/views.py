from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from .models import *
import json




def home(request):
    return render(request, 'home.html')


def vitrin(request):
    vitrin = Item.objects.all()
    serialized = {"vitrin": list(map(lambda vitrin: vitrin.serialize(), Vitrin.objects.all()))}
    json_vitrin = json.dumps(serialized)
    
    return render(request, 'index.html', {'data':json_vitrin} )


