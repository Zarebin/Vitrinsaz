from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import *
import json




def home(request):
    return render(request, 'home.html')


def vitrin(request):
    lessons  = Item.objects.select_related('row')
    serial_lessons = serializers.serialize('json', lessons)
    jsdump = json.dumps(serial_lessons)
    
    return render(request, 'index.html', {'data':jsdump} )


def vitrin_json_response(request):
    vitrin = Item.objects.all()
    serialized = {"vitrin": list(map(lambda vitrin: vitrin.serialize(), Vitrin.objects.all()))}
    print(serialized)
    print('arash')
    print('arash')
    print('arash')
    print('arash')
    json_vitrin = json.dumps(serialized)
    
    return HttpResponse(json_vitrin)

    