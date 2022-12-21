from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse , HttpResponse
from .models import *
import json




def home(request):
    vitrins = Vitrin.objects.all()
    vitrin_json = serializers.serialize('json', vitrins)
    return render(request, 'index.html', {'data':vitrin_json})



def vitrin(request, name:str):
    serialized = {"vitrin":list(map(lambda vitrin: vitrin.serialize(), Vitrin.objects.filter(name__icontains =  name)))}
    vit_json = json.dumps(serialized)

    return render(request, 'home.html', {'data':vit_json})
    

