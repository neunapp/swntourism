# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify
#third library
from datetime import timedelta, datetime
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

#import model

@python_2_unicode_compatible
class Destination(TimeStampedModel):

    name = models.CharField('nombre', max_length=100)
    image = models.URLField('imagen')
    title = models.CharField('titulo', max_length=200)
    content = RichTextUploadingField('contenido')
    slug = models.SlugField(editable=False, max_length=200)
    tags = models.ManyToManyField('miscelanea.Tag')

    class Meta:
        verbose_name = 'destino'
        verbose_name_plural = 'destinos'
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
            slug_unique = '%s %s' % (self.title, str(seconds))
        else:
            seconds = self.slug.split('-')[-1]  # recuperamos los segundos
            slug_unique = '%s %s' % (self.title, str(seconds))

        self.slug = slugify(slug_unique)
        super(Destination, self).save(*args, **kwargs)



@python_2_unicode_compatible
class Gallery(TimeStampedModel):

    name = models.CharField('nombre', max_length=200)
    image = models.URLField('imagen')
    destination = models.ForeignKey(Destination, verbose_name='destino', null=True, blank=True)

    class Meta:
        verbose_name = 'galeria'
        verbose_name_plural = 'galerias'
        ordering = ['-created']

    def __str__(self):
        return  self.name