from django.contrib import admin
from django.utils.html import format_html
from .models import *


@admin.register(Vitrin)
class VitrinAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'vertical_margin', 'horizontal_margin']
    sortable_by = ['id','name']
    list_editable = ['vertical_margin', 'horizontal_margin']
    list_filter = ['name']
    fields = ['name', 'vertical_margin', 'horizontal_margin','style', 'background']



@admin.register(Row)
class RowAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'arrange_type', 'vitrin']
    sortable_by  = ['title']
    list_editable = ['arrange_type']
    list_filter = ['title']
    fields = [ 'title', 'arrange_type', 'radius', 'height', 'ratio', 'vitrin']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'title', 'image_url', 'row', 'image_tag']
    list_editable = ['title', 'image_url']
    list_filter = ['order', 'title']
    sortable_by = ['order', 'title']
    readonly_fields = ['image_tag']
    fields = [ 'title','row', 'image_url', 'image_tag']


    def image_tag(self, obj):
        return format_html('<img src="{url}" width="300" height="200"/>'.format(url = obj.image_url.url))

    image_tag.short_description = 'Image'
