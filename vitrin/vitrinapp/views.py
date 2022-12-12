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

