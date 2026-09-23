from rest_framework import serializers
from .models import Movie, Genre, MyList


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "description",
            "poster_url",
            "backdrop_url",
            "trailer_url",
            "release_year",
            "duration",
            "rating",
            "genres",
            "is_featured",
            "is_trending",
            "created_at",
        ]


class MyListSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(
        read_only=True
    )

    class Meta:
        model = MyList
        fields = [
            "id",
            "movie",
            "created_at",
        ]