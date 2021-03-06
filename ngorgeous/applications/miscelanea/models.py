# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify
#third
from model_utils.models import TimeStampedModel
from datetime import datetime, timedelta
from ckeditor_uploader.fields import RichTextUploadingField
# import models

# Create your models here.
@python_2_unicode_compatible
class Tag(TimeStampedModel):

    name = models.CharField('nombre', max_length=20)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['-created']

    def __str__(self):
        return self.name



@python_2_unicode_compatible
class TestimonialsPackage(TimeStampedModel):

    name = models.CharField('nombre', max_length=70)
    image = models.URLField('imagen')
    commentary = models.TextField('comentario')
    email = models.EmailField('correo')
    packages = models.ForeignKey('paquetes.Package', blank=True, null=True)

    class Meta:
        verbose_name = 'testimonio de paquetes'
        verbose_name_plural = 'testimonios de paquetes'
        ordering = ['-created']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class TestimonialsDestination(TimeStampedModel):

    name = models.CharField('nombre', max_length=70)
    image = models.URLField('imagen')
    commentary = models.TextField('comentario')
    email = models.EmailField('correo')
    destination = models.ForeignKey('destinos.Destination', verbose_name='destino', null=True, blank=True)

    class Meta:
        verbose_name = 'testimonio de destinos'
        verbose_name_plural = 'testimonios de destino'
        ordering = ['-created']

    def __str__(self):
        return self.name



@python_2_unicode_compatible
class Client(TimeStampedModel):

    name = models.CharField('nombre', max_length=200)
    image = models.URLField('imagen')
    facebook = models.CharField('facebook', max_length=200)

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
        ordering = ['-created']

    def __str__(self):
        return self.name



@python_2_unicode_compatible
class Guide(TimeStampedModel):

    name = models.CharField('nombre', max_length=200)
    image = models.URLField('imagen')
    phone = models.CharField('telefono', max_length=13)
    email = models.EmailField('correo')

    class Meta:
        verbose_name = 'guia'
        verbose_name_plural = 'guias'
        ordering = ['-created']

    def __str__(self):
        return self.name