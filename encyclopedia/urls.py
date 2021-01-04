from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:TITLE>", views.entry, name="entry"),
    path("create", views.create, name="create"),
    path("wiki/<str:TITLE>/edit", views.edit, name="edit"),
    path('search', views.search, name="search"),
    path('random', views.random_view, name="random")
]
