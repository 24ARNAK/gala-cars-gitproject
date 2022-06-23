from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):   # created the pic in data table
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.photo.url))  # add photo in models and some code of html

    thumbnail.short_description = 'photo'

    list_display = ('id', 'thumbnail', 'first_name','designation', 'created_date')
    list_display_links = ('id', 'thumbnail', 'first_name',)   # for the id and name be clicket
    search_fields = ('first_name', 'last_name', 'designation')   # for bar the search by name and designation
    list_filter = ('designation',)  # be abel to filter by designation
admin.site.register(Team, TeamAdmin)
