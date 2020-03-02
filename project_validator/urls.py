"""project_validator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crawler.views import table_view, TableListView
# from celery import task
# import threading
from crawler.static.crawler.rss_controller import Crawler

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', table_view, name='home'),
    path('', TableListView.as_view(), name='home'),
]


def start_crawler():
    crawler = Crawler()
    crawler.update_all_feeds()


start_crawler()