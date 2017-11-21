from django.db import models
from filer.fields.image import FilerImageField
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _


class HomePluginModel(CMSPlugin):
    """  plugin para pagina de inicio """
    titulo = models.CharField(max_length=50)

    def copy_relations(self, oldinstance):
        #eliminamos para evitr duplicaados
        self.home_item.all().delete()
        #recuperamos la intancia plugin de la tabla home
        for home_item in oldinstance.home_item.all():
            #
            home_item.pk = None
            home_item.plugin = self
            home_item.save()

    def __str__(self):
        return self.titulo


class ValuePluginModel(CMSPlugin):
    """  plugin para valores de pagina principal """
    titulo = models.CharField(max_length=100)

    def copy_relations(self, oldinstance):
        #eliminamos para evitr duplicaados
        self.values_item.all().delete()
        #recuperamos la intancia plugin de la tabla
        for values_item in oldinstance.values_item.all():
            #
            values_item.pk = None
            values_item.plugin = self
            values_item.save()

    def __str__(self):
        return self.titulo
