# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify
#third import
from datetime import datetime, timedelta
from model_utils.models import TimeStampedModel
#import models



@python_2_unicode_compatible
class Package(TimeStampedModel):

    name = models.CharField('nombre', max_length=100)
    image = models.URLField('imagen')
    resume = models.TextField('resumen')
    days = models.IntegerField('dias')
    short_description = models.TextField('descripcion corta')
    price = models.IntegerField('precio')
    tags = models.ManyToManyField('miscelanea.Tag', blank=True)

    class Meta:
        verbose_name = 'paquete'
        verbose_name_plural = 'paquetes'
        ordering = ['-created']

    def __str__(self):
        return self.name

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
            slug_unique = '%s %s' % (self.name, str(seconds))
        else:
            seconds = self.slug.split('-')[-1]  # recuperamos los segundos
            slug_unique = '%s %s' % (self.name, str(seconds))

        self.slug = slugify(slug_unique)
        super(Package, self).save(*args, **kwargs)



@python_2_unicode_compatible
class Route(TimeStampedModel):

    order = models.CharField('orden', max_length=200)
    package = models.ForeignKey(Package, verbose_name='paquete')
    destination = models.ForeignKey('destinos.Destination', verbose_name='destino', blank=True, null=True)

    class Meta:
        verbose_name = 'ruta'
        verbose_name_plural = 'rutas'
        ordering = ['-created']

    def __str__(self):
        return self.order



@python_2_unicode_compatible
class Property(TimeStampedModel):

    order = models.IntegerField('orden')
    content = models.TextField('contenido')
    route = models.ForeignKey(Route, verbose_name='rutas')

    class Meta:
        verbose_name = 'propiedad'
        verbose_name_plural = 'propiedades'
        ordering = ['-created']

    def __str__(self):
        return self.order






