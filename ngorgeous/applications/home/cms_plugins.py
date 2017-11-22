#django-cms
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
#django
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
#local pass
from .cms_models import HomePluginModel, ValuePluginModel
from .models import Home, Values


class HomeInlineAdmin(admin.StackedInline):
    model = Home
    extra = 1


class ValuesInlineAdmin(admin.StackedInline):
    model = Values


@plugin_pool.register_plugin
class HomePlugin(CMSPluginBase):
    model = HomePluginModel
    name = _("Portada Principal")
    render_template = "home/plugins/banner.html"
    inlines = (HomeInlineAdmin, )
    cache = False

    def render(self, context, instance, placeholder):
        context = super(HomePlugin, self).render(context, instance, placeholder)
        homes = instance.home_item.all()
        if homes.count() > 0:
            context.update({
                'home': homes[0]
            })
        return context


@plugin_pool.register_plugin
class ValuesPlugin(CMSPluginBase):
    model = ValuePluginModel
    name = _("Valores pagina principal")
    render_template = "home/plugins/values.html"
    inlines = (ValuesInlineAdmin, )
    cache = False

    def render(self, context, instance, placeholder):
        context = super(ValuesPlugin, self).render(context, instance, placeholder)
        values = instance.values_item.all()
        context.update({
            'values': values
        })
        return context
