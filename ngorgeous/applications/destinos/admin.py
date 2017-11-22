# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

#
from .models import Destination, Gallery

admin.site.register(Destination)
admin.site.register(Gallery)
