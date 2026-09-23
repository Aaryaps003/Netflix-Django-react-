from django.core.management.base import BaseCommand
from movies.models import Movie, Genre


MOVIES = [
    {
        "title": "Neon Horizon",
        "description": "A futuristic detective discovers a hidden network controlling the city's digital infrastructure.",
        "poster_url": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba",
        "backdrop_url": "https://images.unsplash.com/photo-1485846234645-a62644f84728",
        "release_year": 2026,
        "duration": 124,
        "rating": 8.4,
        "genres": ["Sci-Fi", "Thriller"],
        "featured": True,
        "trending": True,
    },
    {
        "title": "The Last Signal",
        "description": "A mysterious transmission from deep space changes everything humanity knows about the universe.",
        "poster_url": "https://images.unsplash.com/photo-1440404653325-ab127d49abc1",
        "backdrop_url": "https://images.unsplash.com/photo-1446776877081-d282a0f896e2",
        "release_year": 2025,
        "duration": 137,
        "rating": 8.7,
        "genres": ["Sci-Fi", "Drama"],
        "featured": False,
        "trending": True,
    },
    {
        "title": "Midnight Run",
        "description": "An ordinary courier gets caught in a dangerous conspiracy during one unforgettable night.",
        "poster_url": "https://images.unsplash.com/photo-1487180149984-4e4e0f6f4e7b",
        "backdrop_url": "https://images.unsplash.com/photo-1519608487953-e999c86e7455",
        "release_year": 2025,
        "duration": 118,
        "rating": 8.1,
        "genres": ["Action", "Thriller"],
        "featured": False,
        "trending": True,
    },
    {
        "title": "Parallel",
        "description": "A scientist discovers a doorway to another version of Earth where one decision changed everything.",
        "poster_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401",
        "backdrop_url": "https://images.unsplash.com/photo-1500534623283-312aade485b7",
        "release_year": 2024,
        "duration": 131,
        "rating": 8.6,
        "genres": ["Sci-Fi", "Drama"],
        "featured": False,
        "trending": True,
    },
    {
        "title": "Zero Hour",
        "description": "A cybersecurity analyst has sixty minutes to stop a global attack.",
        "poster_url": "https://images.unsplash.com/photo-1518770660439-4636190af475",
        "backdrop_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23",
        "release_year": 2024,
        "duration": 112,
        "rating": 7.9,
        "genres": ["Action", "Thriller"],
        "featured": False,
        "trending": True,
    },
    {
        "title": "After Tomorrow",
        "description": "A family attempts to rebuild their lives after a mysterious global event.",
        "poster_url": "https://images.unsplash.com/photo-1536440136628-849c177e76a1",
        "backdrop_url": "https://images.unsplash.com/photo-1500534623283-312aade485b7",
        "release_year": 2023,
        "duration": 126,
        "rating": 8.0,
        "genres": ["Drama", "Sci-Fi"],
        "featured": False,
        "trending": False,
    },
    {
        "title": "The Heist",
        "description": "A group of specialists plans an impossible robbery against the world's most secure vault.",
        "poster_url": "https://images.unsplash.com/photo-1561214115-f2f134cc4912",
        "backdrop_url": "https://images.unsplash.com/photo-1560179707-f14e90ef3623",
        "release_year": 2022,
        "duration": 119,
        "rating": 8.3,
        "genres": ["Crime", "Thriller", "Action"],
        "featured": False,
        "trending": False,
    },
    {
        "title": "Summer Nights",
        "description": "Four friends discover that growing up doesn't mean leaving everything behind.",
        "poster_url": "https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f",
        "backdrop_url": "https://images.unsplash.com/photo-1470252649378-9c29740c9fa8",
        "release_year": 2023,
        "duration": 108,
        "rating": 7.6,
        "genres": ["Drama", "Romance"],
        "featured": False,
        "trending": False,
    },
    {
        "title": "Dark Matter",
        "description": "A physicist uncovers evidence that reality may be far stranger than anyone imagined.",
        "poster_url": "https://images.unsplash.com/photo-1534791547706-7b57566a0f58",
        "backdrop_url": "https://images.unsplash.com/photo-1462331940025-496dfbfc7564",
        "release_year": 2025,
        "duration": 129,
        "rating": 8.5,
        "genres": ["Sci-Fi", "Mystery", "Thriller"],
        "featured": False,
        "trending": True,
    },
    {
        "title": "The Final Game",
        "description": "A young athlete gets one final chance to prove that talent is only part of winning.",
        "poster_url": "https://images.unsplash.com/photo-1461896836934-ffe607ba8211",
        "backdrop_url": "https://images.unsplash.com/photo-1461896836934-ffe607ba8211",
        "release_year": 2024,
        "duration": 115,
        "rating": 8.2,
        "genres": ["Drama"],
        "featured": False,
        "trending": False,
    },
]


class Command(BaseCommand):
    help = "Seeds the database with sample Netflix-style movies."

    def handle(self, *args, **options):

        self.stdout.write("Creating genres...")

        for movie_data in MOVIES:
            for genre_name in movie_data["genres"]:
                Genre.objects.get_or_create(name=genre_name)

        self.stdout.write("Creating movies...")

        for movie_data in MOVIES:

            movie, created = Movie.objects.get_or_create(
                title=movie_data["title"],
                defaults={
                    "description": movie_data["description"],
                    "poster_url": movie_data["poster_url"],
                    "backdrop_url": movie_data["backdrop_url"],
                    "release_year": movie_data["release_year"],
                    "duration": movie_data["duration"],
                    "rating": movie_data["rating"],
                    "is_featured": movie_data["featured"],
                    "is_trending": movie_data["trending"],
                },
            )

            for genre_name in movie_data["genres"]:
                genre = Genre.objects.get(name=genre_name)
                movie.genres.add(genre)

            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Created: {movie.title}"
                    )
                )
            else:
                self.stdout.write(
                    f"Already exists: {movie.title}"
                )

        self.stdout.write(
            self.style.SUCCESS(
                "\nMovie database seeded successfully!"
            )
        )