from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("error/", views.error_page, name="error"),
    path("search/", views.search_page, name="search"),
    path("new-page/", views.new_page, name="new_page"),
    path("edit-page/<str:title>", views.edit_page, name="edit_page"),
    path("random-page/", views.random_page, name="random_page")
]
