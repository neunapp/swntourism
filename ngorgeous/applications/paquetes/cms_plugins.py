#django-cms
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
#django
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
#local pass
from .cms_models import PackagePluginModel
from .models import Package


class PackageInlineAdmin(admin.StackedInline):
    model = Package


@plugin_pool.register_plugin
class PackagePlugin(CMSPluginBase):
    model = PackagePluginModel
    name = _("Lista de ultimo paquetes turisticos")
    render_template = "paquetes/plugins/list.html"
    inlines = (PackageInlineAdmin, )
    cache = False

    def render(self, context, instance, placeholder):
        context = super(PackagePlugin, self).render(context, instance, placeholder)
        paquetes = instance.package_item.all()
        context.update({
            'paquetes': paquetes
        })
        return context
