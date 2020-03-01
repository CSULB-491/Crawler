# this one doesn't match with the other url. If problems, investigate here

from django.conf.urls import url
from . import views

urlpatterns = [
    # /publisher/
    url(r'^$', views.index, name='index'),

    # /publisher/712/   what ?<publisher_id> this is like a variable. This is how django made it. It's weird, but works
    # stores it in that weird variable then passes it through that method
    # name='detail' is just the function name from the 'views' function
    # what this does is pulls out the number from publisher --> publisher/number/ and stores it into that variable.
    url(r'^(?P<publisher_id>[0-9]+)/$', views.detail, name='detail'),
]