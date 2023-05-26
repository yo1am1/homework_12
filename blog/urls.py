from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("publications/", views.publications, name="publications"),
    path("publications/<int:id>/", views.publication, name="publication"),
]
