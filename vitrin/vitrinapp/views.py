from django.shortcuts import render
from django.core import serializers
from .models import *




def home(request):
    return render(request, 'home.html')




def news(request):
    news = News.objects.all()
    serialize_news = serializers.serialize('json', news)

    return render(request, 'index.html',{'data':serialize_news})




def animations(request):
    animations = Animation.objects.all()
    serialize_animations = serializers.serialize('json', animations)

    return render(request, 'index.html', {'data':serialize_animations} )



def educations(request):
    educations = Education.objects.all()
    serialize_educations  = serializers.serialize('json', educations)

    return render(request, 'index.html', {'data':serialize_educations} )
