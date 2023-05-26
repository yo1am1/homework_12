from django.shortcuts import render

from blog.models import Publication


def index(request):
    Publication.objects.create(title="First blog", content="First blog content right here!")
    pub = Publication.objects.get(id=id)
    return render(request, 'index.html', {})


def publications(request):

    return render(request, 'publications.html', {})


def publication(request, id):
    pass
