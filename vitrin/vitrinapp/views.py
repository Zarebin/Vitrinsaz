from django.shortcuts import render
from django.core import serializers
from .models import *
import json




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
    ss = serializers.serialize('json', educations)
#     serialize_educations = {
#   "name": "بازار",
#   "theme": {

#   },
#   "rows": [
#     {
#       "header": {
#         "title": "پایه هفتم"
#       },
#       "arrange_type": "fixed_width",
#       "item_style": {
#         # "radius": True,
#         "ratio": 66.66
#       },
#       "items": ss
#     }
#   ]
# }

    serialize_educations = {
    "name": "بازار",
    "theme": {
      
    },
    "rows": [
      {
        "header": {
          "title": "پایه هفتم"
          
        },
        "arrange_type": "fixed_height",
        "item_style": {
            "radius": True,
            "ratio": 66.66
          },
        "items": [
          {
            "order": 0,
            "image_url": "https://img.freepik.com/free-photo/beautiful-shot-sunrise-country-road-netherlands_181624-29198.jpg?t=st=1670786747~exp=1670787347~hmac=fec5e421e073d241b963bfc47e293c7bc8afba4fc4d605075331cbf4314063b5",
            "title": "فارسی",
            "url": "http://"
          },
          {
            "order": 1,
            "image_url": "https://img.freepik.com/free-photo/beautiful-aerial-shot-fronalpstock-mountains-switzerland-beautiful-pink-blue-sky_181624-9315.jpg?t=st=1670786857~exp=1670787457~hmac=075cf03e209f2540023896b744382f01946a070835f931e5fd21777547b5462c",
            "title": "ریاضی",
            "url": "http:/"
          },
          {
            "order": 2,
            "image_url": "https://img.freepik.com/free-photo/beautiful-aerial-shot-fronalpstock-mountains-switzerland-beautiful-pink-blue-sky_181624-9315.jpg?t=st=1670786857~exp=1670787457~hmac=075cf03e209f2540023896b744382f01946a070835f931e5fd21777547b5462c",
            "url": "http://",
            "title": "انگلیسی"
          },
          {
            "order": 3,
            "image_url": "https://img.freepik.com/free-photo/beautiful-aerial-shot-fronalpstock-mountains-switzerland-beautiful-pink-blue-sky_181624-9315.jpg?t=st=1670786857~exp=1670787457~hmac=075cf03e209f2540023896b744382f01946a070835f931e5fd21777547b5462c",
            "url": "http://",
            "title": "انگلیسی"
          }
        ]
      },



	 {
        "header": {
          "title": "پایه هفتم"
          
        },
        "arrange_type": "fixed_height",
        "item_style": {
            "radius": True,
            "ratio": 66.66
          },
        "items": [
          {
            "order": 0,
            "image_url": "https://img.freepik.com/free-photo/beautiful-shot-sunrise-country-road-netherlands_181624-29198.jpg?t=st=1670786747~exp=1670787347~hmac=fec5e421e073d241b963bfc47e293c7bc8afba4fc4d605075331cbf4314063b5",
            "title": "فارسی",
            "url": "http://"
          },
          {
            "order": 1,
            "image_url": "https://img.freepik.com/free-photo/beautiful-aerial-shot-fronalpstock-mountains-switzerland-beautiful-pink-blue-sky_181624-9315.jpg?t=st=1670786857~exp=1670787457~hmac=075cf03e209f2540023896b744382f01946a070835f931e5fd21777547b5462c",
            "title": "ریاضی",
            "url": "http:/"
          },
          {
            "order": 2,
            "image_url": "https://img.freepik.com/free-photo/beautiful-aerial-shot-fronalpstock-mountains-switzerland-beautiful-pink-blue-sky_181624-9315.jpg?t=st=1670786857~exp=1670787457~hmac=075cf03e209f2540023896b744382f01946a070835f931e5fd21777547b5462c",
            "url": "http://",
            "title": "انگلیسی"
          },
          {
            "order": 3,
            "image_url": "https://img.freepik.com/free-photo/beautiful-aerial-shot-fronalpstock-mountains-switzerland-beautiful-pink-blue-sky_181624-9315.jpg?t=st=1670786857~exp=1670787457~hmac=075cf03e209f2540023896b744382f01946a070835f931e5fd21777547b5462c",
            "url": "http://",
            "title": "انگلیسی"
          }
        ]
      }



    ]
  }
    jsdump = json.dumps(serialize_educations)
    print(serialize_educations)
    return render(request, 'index.html', {'data':jsdump} )
