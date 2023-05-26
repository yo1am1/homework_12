from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("publications/<int:id>/", views.publications, name="publications"),
]
