from django.shortcuts import render
from django.core import serializers
from .models import *
import json




def home(request):
    vitrins = Vitrin.objects.all()
    vitrin_json = serializers.serialize('json', vitrins)
    return render(request, 'index.html', {'data':vitrin_json, 'vitrins':vitrins})



def vitrin(request, name:str):
    vitrin = Vitrin.objects.filter(name__icontains =  name)
    serialized = {"vitrin":list(map(lambda vitrin: vitrin.serialize(), vitrin))}
    vitrin_data = json.dumps(serialized, ensure_ascii=False, indent=4)
    return render(request, 'education.html', {'data':vitrin_data, 'vitrin':vitrin})

    

