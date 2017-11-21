from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
#
from django.contrib.sitemaps.views import sitemap

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #url for django csm
    url(r'^', include('cms.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
