# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify
# third-party
from model_utils.models import TimeStampedModel
from datetime import datetime, timedelta
from colorfield.fields import ColorField
#django-cms models
from .cms_models import HomePluginModel, ValuePluginModel
#miscelanea

# Create your models here.

@python_2_unicode_compatible
class Home(TimeStampedModel):

    title = models.CharField('titulo', max_length=200, blank=True)
    subtitle = models.CharField('subtitulo', max_length=200, blank=True)
    coverpage = models.ImageField('portada', upload_to='home', blank=True, null=True)
    button_primary = models.CharField('boton primario', max_length=200, blank=True)
    button_secundary = models.CharField('boton secundario', max_length=200, blank=True)
    slug = models.SlugField(editable=False, max_length=200)
    #
    plugin = models.ForeignKey(
        HomePluginModel,
        related_name="home_item"
    )
    class Meta:
        verbose_name = 'Pagina Principal'
        verbose_name_plural = 'Pagina Principal'
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



@python_2_unicode_compatible
class Values(TimeStampedModel):
    """django data model valores en el home"""

    value = models.CharField('Valor', max_length=30)
    icon = models.CharField('icono', max_length=30)
    color = ColorField(default='#1976D2')
    description = models.CharField('Descripcion', max_length=100)
    #
    plugin = models.ForeignKey(
        ValuePluginModel,
        related_name="values_item"
    )

    class Meta:
        verbose_name = 'Valores'
        verbose_name_plural = 'Valores pagina principal'
        ordering = ['-created']

    def __str__(self):
        return self.value
