from django.conf.urls import url

from . import views

app_name = 'publisher'

urlpatterns = [
       # /publisher/
       url(r'^$', views.index, name='index'),
       # /publisher/<publisher_id>/
       url(r'^(?P<publisher_id>[0-9]+)/$', views.detail, name='detail'),
       # /publisher/(?P<pk>[0-9]+)/<author_id>/
       url(r'^(?P<publisher_id>[0-9]+)/(?P<author_id>[0-9]+)/$', views.author_index, name='author_index'),
       # /publisher/publisher/add/
       url(r'publisher/add/$', views.create_publisher, name='create_publisher'),

       # /publisher/1
       url(r'(?P<publisher_id>[0-9]+)/$', views.update_publisher, name='update_publisher'),
       url(r'(?P<publisher_id>[0-9]+)/$', views.delete_publisher, name='delete_publisher'),

]
