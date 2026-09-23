from django.urls import path

from .views import (
    MovieListView,
    MovieDetailView,
    MyListView,
    AddToMyListView,
    RemoveFromMyListView,
)


urlpatterns = [

    path(
        "my-list/",
        MyListView.as_view(),
        name="my-list"
    ),

    path(
        "my-list/add/<int:movie_id>/",
        AddToMyListView.as_view(),
        name="add-to-my-list"
    ),

    path(
        "my-list/remove/<int:movie_id>/",
        RemoveFromMyListView.as_view(),
        name="remove-from-my-list"
    ),

    path(
        "",
        MovieListView.as_view(),
        name="movie-list"
    ),

    path(
        "<int:pk>/",
        MovieDetailView.as_view(),
        name="movie-detail"
    ),
]