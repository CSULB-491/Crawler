from django.shortcuts import render, get_object_or_404

from .forms import PublisherForm
from .models import Publisher, Author, Article
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

# from django.http import HttpResponse
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


def author_index(request, publisher_id, author_id):
    publisher = get_object_or_404(Publisher, pk=publisher_id)
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'publisher/author_index.html', {'publisher': publisher, 'author': author})


def create_publisher(request, IMAGE_FILE_TYPES=None):
    # if not request.user.is_authenticated():
    # return render(request, 'publisher/login.html')
    # else:
    form = PublisherForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        publisher = form.save(commit=False)
        # publisher.user = request.user
        # publisher.publisher_logo = request.FILES['publisher_logo']
        # file_type = publisher.publisher_logo.url.split('.')[-1]
        # file_type = file_type.lower()
        # if file_type not in IMAGE_FILE_TYPES:
        #     context = {
        #        'publisher': publisher,
        #        'form': form,
        #        'error_message': 'Image file must be PNG, JPG, or JPEG',
        #    }
        #    return render(request, 'publisher/create_publisher.html', context)
        publisher.save()
        return render(request, 'publisher/detail.html', {'publisher': publisher})
    context = {
        "form": form,
    }
    return render(request, 'publisher/create_publisher.html', context)


def update_publisher(request):
    form = PublisherForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        publisher = form.save(commit=False)
        publisher.save()
        return render(request, 'publisher/detail.html', {'publisher': publisher})
    context = {
        "form": form,
    }
    return render(request, 'publisher/create_publisher.html', context)


def delete_publisher(request, publisher_id):
    publisher = Publisher.objects.get(pk=publisher_id)
    publisher.delete()
    publisher = Publisher.objects.filter(user=request.user)
    return render(request, 'publisher/index.html', {'publishers': publisher})


"""
def author_detail(request, publisher_id, author_id, article_id):
    publisher = get_object_or_404(Publisher, pk=publisher_id)
    author = get_object_or_404(Author, pk=author_id)
    article = get_object_or_404(article_id)
    return render(request, 'publisher/author/author_detail.html', {'article': article})
"""
