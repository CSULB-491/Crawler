from django.shortcuts import render, get_object_or_404
from .models import Publisher, Author, Article
from django.http import HttpResponse
# every single view function takes the request and the request is the html request. Whenever a user
# connects to the site and requests something, like webpage, image, and stuff.


# by default, django is already setup to look at your templates directory on your apps directory,
# in this case, publisher
def index(request):
    all_publishers = Publisher.objects.all()
    return render(request, 'publisher/index.html', {'all_publishers': all_publishers})


def detail(request, publisher_id):
    publisher = get_object_or_404(Publisher, pk=publisher_id)
    return render(request, 'publisher/detail.html', {'publisher': publisher})


def author_detail(request, publisher_id, author_id):
    publisher = get_object_or_404(Publisher, pk=publisher_id)
    author = get_object_or_404(Author, pk=author_id)
    all_authors = Author.objects.all()
    return render(request, 'publisher/author_detail.html', {'author': author})

