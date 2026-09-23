from django.contrib import admin

from .models import Genre, Movie


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "release_year",
        "rating",
        "duration",
        "is_featured",
        "is_trending",
    )

    list_filter = (
        "is_featured",
        "is_trending",
        "release_year",
        "genres",
    )

    search_fields = (
        "title",
        "description",
    )

    filter_horizontal = ("genres",)