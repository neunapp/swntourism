from django.db import models
from filer.fields.image import FilerImageField
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
#


class PackagePluginModel(CMSPlugin):
    """  plugin para paquetes turisticos """
    titulo = models.CharField(max_length=50)

    def copy_relations(self, oldinstance):
        #eliminamos para evitr duplicaados
        self.package_item.all().delete()
        #recuperamos la intancia plugin de la tabla home
        for package_item in oldinstance.package_item.all():
            #
            package_item.pk = None
            package_item.plugin = self
            package_item.save()

    def __str__(self):
        return self.titulo
