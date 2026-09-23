from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Movie, MyList
from .serializers import (
    MovieSerializer,
    MyListSerializer,
)


class MovieListView(generics.ListAPIView):

    queryset = Movie.objects.all().order_by("-created_at")
    serializer_class = MovieSerializer


class MovieDetailView(generics.RetrieveAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MyListView(generics.ListAPIView):

    serializer_class = MyListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MyList.objects.filter(
            user=self.request.user
        ).select_related(
            "movie"
        ).prefetch_related(
            "movie__genres"
        )


class AddToMyListView(generics.CreateAPIView):

    serializer_class = MyListSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):

        movie_id = kwargs.get("movie_id")

        try:
            movie = Movie.objects.get(
                id=movie_id
            )
        except Movie.DoesNotExist:

            return Response(
                {
                    "error": "Movie not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        my_list, created = MyList.objects.get_or_create(
            user=request.user,
            movie=movie
        )

        if not created:

            return Response(
                {
                    "message": "Movie is already in your list."
                },
                status=status.HTTP_200_OK
            )

        serializer = self.get_serializer(
            my_list
        )

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


class RemoveFromMyListView(generics.DestroyAPIView):

    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):

        movie_id = kwargs.get("movie_id")

        try:
            my_list = MyList.objects.get(
                user=request.user,
                movie_id=movie_id
            )

        except MyList.DoesNotExist:

            return Response(
                {
                    "error": "Movie is not in your list."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        my_list.delete()

        return Response(
            {
                "message": "Movie removed from your list."
            },
            status=status.HTTP_200_OK
        )