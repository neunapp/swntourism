# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
#
from .models import (
    Client,
    TestimonialsDestination,
    Tag,
    TestimonialsPackage,
    Guide
)

admin.site.register(Client)
admin.site.register(TestimonialsDestination)
admin.site.register(TestimonialsPackage)
admin.site.register(Guide)
admin.site.register(Tag)
