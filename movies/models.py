from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    poster_url = models.URLField()

    backdrop_url = models.URLField(
        blank=True
    )

    trailer_url = models.URLField(
        blank=True
    )

    release_year = models.PositiveIntegerField()

    duration = models.PositiveIntegerField(
        help_text="Duration in minutes"
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1
    )

    genres = models.ManyToManyField(
        Genre,
        related_name="movies"
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_trending = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class MyList(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="my_list"
    )

    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="added_by_users"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "movie"],
                name="unique_user_movie"
            )
        ]

        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"