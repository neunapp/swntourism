# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify
#third library
from ckeditor_uploader.fields import RichTextUploadingField
from model_utils.models import TimeStampedModel
from datetime import datetime, timedelta
#import modelsf
from applications.miscelanea.models import Tag, Guide, Client
# Create your models here.



@python_2_unicode_compatible
class Experience(TimeStampedModel):

    name = models.CharField('nombre', max_length=100)
    image = models.URLField('imagen')
    video = models.URLField('video')
    first_image = models.URLField('primer imagen')
    second_image = models.URLField('segunda imagen')
    third_image = models.URLField('tecer imagen')
    guide = models.ForeignKey(Guide, verbose_name='guia')
    guide_experience = RichTextUploadingField('experiencia del guia')
    client = models.ForeignKey(Client, verbose_name='cliente')
    client_experience = RichTextUploadingField('experiencia del cliente')
    slug = models.SlugField(editable=False, max_length=200)
    tags = models.ManyToManyField(Tag)

    class Meta:

        verbose_name = 'Experiencia'
        verbose_name_plural = 'Experiencias'
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
        super(Experience, self).save(*args, **kwargs)