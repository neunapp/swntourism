# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify
# third-party
from model_utils.models import TimeStampedModel
from datetime import datetime, timedelta

#miscelanea
from applications.miscelanea.models import Tag
# Create your models here.

@python_2_unicode_compatible
class Home(TimeStampedModel):

    title = models.CharField('titulo', max_length=200)
    subtitle = models.CharField('subtitulo', max_length=200)
    coverpage = models.ImageField('portada')
    button_primary = models.CharField('boton primario', max_length=200)
    button_secundary = models.CharField('boton secundario', max_length=200)
    first_value = models.CharField('primer valor', max_length=200)
    first_value_content = models.TextField('contenido primer valor')
    second_value = models.CharField('segundo valor', max_length=200)
    second_value_content = models.TextField('contenido segundo valor')
    third_value = models.CharField('tercer valor', max_length=200)
    third_value_content = models.TextField('contenido tercer valor')
    first_subtitle = models.CharField('primer subtitulo', max_length=200)
    first_subtitle_description = models.CharField('descripcion primer subtitulo', max_length=300)
    second_subtitle = models.CharField('segundo subtitulo', max_length=200)
    second_subtitle_description = models.CharField('descripcion segundo subtitulo', max_length=300)
    third_subtitle = models.CharField('tercer subtitulo', max_length=200)
    slug = models.SlugField(editable=False, max_length=200)
    third_subtitle_description = models.CharField('descripcion tercer subtitulo', max_length=300)
    phone = models.CharField('telefono', max_length=12)
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Homes'
        ordering = ['-created']

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.id:
            # calculamos el total de segundos de la hora actual
            now = datetime.now()
            total_time = timedelta(
                hours=now.hour,
                minutes=now.minute,
                seconds=now.second
            )
            seconds = int(total_time.total_seconds())
            slug_unique = '%s %s' % (self.title, str(seconds))
        else:
            seconds = self.slug.split('-')[-1]  # recuperamos los segundos
            slug_unique = '%s %s' % (self.title, str(seconds))

        self.slug = slugify(slug_unique)
        super(Home, self).save(*args, **kwargs)