from django.contrib import admin
from django.utils.html import format_html
from .models import *


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'image_tag']
    sortable_by = ['title', 'category']
    list_editable = ['title']
    list_filter = ['category']
    readonly_fields = ['image_tag']
    fields = ['title', 'category','image_url', 'image_tag', 'news_text']


    def image_tag(self, obj):
        return format_html('<img src="{url}" width="300" height="200"/>'.format(url = obj.image_url.url))

    image_tag.short_description = 'Image'



@admin.register(Animation)
class AnimationAdmin(admin.ModelAdmin):
    list_display = ['id', 'animation_name', 'genre', 'image_tag']
    sortable_by  = ['animation_name', 'genre']
    list_editable = ['animation_name']
    list_filter = ['genre']
    readonly_fields = ['image_tag']
    fields = [ 'animation_name', 'genre', 'image_url', 'image_tag','summary']


    def image_tag(self, obj):
        return format_html('<img src="{url}" width="300" height="200"/>'.format(url = obj.image_url.url))

    image_tag.short_description = 'Image'


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'title', 'image_tag']
    list_editable = ['title']
    list_filter = ['order']
    sortable_by = ['order', 'title']
    readonly_fields = ['image_tag']
    fields = ['order', 'title', 'image_url', 'image_tag']


    def image_tag(self, obj):
        return format_html('<img src="{url}" width="300" height="200"/>'.format(url = obj.image_url.url))

    image_tag.short_description = 'Image'
