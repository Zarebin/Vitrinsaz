from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('vitrin/', vitrin, name='vitrin'),
    path('vitrinjson/', vitrin_json_response, name='vitrinjson'),
]