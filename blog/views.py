from django.shortcuts import render

from blog.models import Publication


def index(request):
    return render(request, "index.html", {})


def publication(request, id):
    pub = Publication.objects.get(id=id)
    name = pub.title
    content = pub.content
    time = pub.updated_at
    return render(request, "publications.html", {"name": name, "content": content, "time": time})
