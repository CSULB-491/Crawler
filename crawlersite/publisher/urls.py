# this one doesn't match with the other url. If problems, investigate here

from django.conf.urls import url
from . import views

app_name = 'publisher'

urlpatterns = [
    # /publisher/
    url(r'^$', views.index, name='index'),

    # /publisher/<publisher_id>/
    url(r'^(?P<publisher_id>[0-9]+)/$', views.detail, name='detail'),

    # /publisher/<publisher_id>/<author_id>/
    url(r'^(?P<publisher_id>[0-9]+)/(?P<author_id>[0-9]+)/$', views.author_detail, name='author_detail'),
]
