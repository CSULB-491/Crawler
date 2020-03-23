from django.contrib import admin
from django.conf.urls import include, url
# from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^publisher/', include('publisher.urls')),
    url(r'^publisher/(?P<publisher_id>[0-9]+)/', include('publisher.urls')),
    url(r'^publisher/(?P<publisher_id>[0-9]+)/(?P<author_id>[0-9]+)/', include('publisher.urls')),
    url(r'publisher/add/', include('publisher.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

