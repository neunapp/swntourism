# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Package, Route, Property

class PackageAdmin(admin.ModelAdmin):
   list_display = (
       'name',
       'short_description',
       'days',
       'price',
       'plugin'
   )
   search_fields = ('name',)
   list_filter = ('price',)
   #campos para agregar
   #
   filter_horizontal = ('tags',)

admin.site.register(Package, PackageAdmin)
admin.site.register(Route)
admin.site.register(Property)
