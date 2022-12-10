from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('news/', news, name='news'),
    path('animations/', animations, name='animaions'),
    path('educations/', educations, name='educations'),
    path('admin/', admin.site.urls),
]
