from django.http import Http404
from django.shortcuts import render
from .models import Publisher

# every single view function takes the request and the request is the html request. Whenever a user
# connects to the site and requests something, like webpage, image, and stuff.


# by default, django is already setup to look at your templates directory on your apps directory,
# in this case, publisher
def index(request):
    all_publishers = Publisher.objects.all()
    # context = {'all_publishers': all_publishers}
    return render(request, 'publisher/index.html', {'all_publishers': all_publishers})


def detail(request, publisher_id):
    try:
        publisher = Publisher.objects.get(pk=publisher_id)
    except Publisher.DoesNotExist:
        raise Http404("Publisher does not exist")
    return render(request, 'publisher/detail.html', {'publisher': publisher})
