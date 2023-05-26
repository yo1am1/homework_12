from django.shortcuts import render
from django.views.decorators.cache import cache_page

from blog.models import Publication


def index(request):
    return render(request, "index.html", {})


@cache_page(60 * 15)
def publications(request, id=None):
    try:
        pub = Publication.objects.get(id=id)
    except:
        return render(request, "publications.html", {"error": "No such publication"})

    name = pub.title
    content = pub.content
    time = pub.updated_at
    return render(
        request, "publications.html", {"name": name, "content": content, "time": f"({time})"}
    )
