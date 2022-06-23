from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.


class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):  # created the pic in data table
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.car_photo.url))

    thumbnail.short_description = 'Car Image'
    list_display = ('id','thumbnail', 'car_title', 'city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')  # show element in table
    list_display_links = ('id', 'thumbnail', 'car_title') # for the id and name be clicket
    list_editable = ('is_featured',)
    search_fields = ('car_title', 'city', 'model', 'body_style', 'fuel_type')  # for bar the search by element
    list_filter = ('city', 'model', 'body_style' , 'fuel_type') # be abel to filter by element
admin.site.register(Car, CarAdmin)
