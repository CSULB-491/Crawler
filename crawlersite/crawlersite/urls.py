from django.contrib import admin
from django.conf.urls import include, url
# from django.urls import include, path


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^publisher/', include('publisher.urls')),
    url(r'^publisher/(?P<publisher_id>[0-9]+)/', include('publisher.urls')),
    url(r'^publisher/(?P<publisher_id>[0-9]+)/(?P<author_id>[0-9]+)/', include('publisher.urls')),
]

