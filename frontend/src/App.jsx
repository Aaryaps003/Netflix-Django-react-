import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

const API_URL = "http://127.0.0.1:8000/api/movies/";

function App() {
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [search, setSearch] = useState("");
  const [selectedMovie, setSelectedMovie] = useState(null);

  useEffect(() => {
    axios
      .get(API_URL)
      .then((response) => {
        const data = response.data;

        setMovies(
          Array.isArray(data)
            ? data
            : data.results || []
        );
      })
      .catch((err) => {
        console.error(err);
        setError(
          "Could not load movies. Make sure Django is running."
        );
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  const featuredMovie =
    movies.find((movie) => movie.is_featured) || movies[0];

  const trendingMovies = movies.filter(
    (movie) => movie.is_trending
  );

  const filteredMovies = movies.filter((movie) =>
    movie.title
      .toLowerCase()
      .includes(search.toLowerCase())
  );

  const getByGenre = (genreName) => {
    return movies.filter((movie) =>
      movie.genres?.some(
        (genre) =>
          genre.name.toLowerCase() ===
          genreName.toLowerCase()
      )
    );
  };

  const openMovie = (movie) => {
    setSelectedMovie(movie);
    document.body.style.overflow = "hidden";
  };

  const closeMovie = () => {
    setSelectedMovie(null);
    document.body.style.overflow = "auto";
  };

  return (
    <div className="app">

      {/* ================= NAVBAR ================= */}

      <nav className="navbar">

        <div className="logo">
          NETFLIX
        </div>

        <div className="nav-links">
          <span>Home</span>
          <span>TV Shows</span>
          <span>Movies</span>
          <span>New & Popular</span>
          <span>My List</span>
        </div>

        <div className="nav-right">

          <div className="search-container">

            <span className="search-icon">
              🔍
            </span>

            <input
              type="text"
              placeholder="Search titles..."
              value={search}
              onChange={(e) =>
                setSearch(e.target.value)
              }
            />

          </div>

          <span className="notification">
            🔔
          </span>

          <div className="profile">
            A
          </div>

        </div>

      </nav>


      {/* ================= SEARCH RESULTS ================= */}

      {search && (
        <section className="search-results">

          <h2>
            Search results for "{search}"
          </h2>

          {filteredMovies.length === 0 ? (
            <p className="no-results">
              No movies found.
            </p>
          ) : (

            <div className="search-grid">

              {filteredMovies.map((movie) => (

                <MovieCard
                  key={movie.id}
                  movie={movie}
                  onClick={() => openMovie(movie)}
                />

              ))}

            </div>

          )}

        </section>
      )}


      {/* ================= HERO ================= */}

      {!search && featuredMovie && (

        <section
          className="hero"
          style={{
            backgroundImage: `
              linear-gradient(
                to right,
                rgba(0,0,0,0.95) 0%,
                rgba(0,0,0,0.75) 35%,
                rgba(0,0,0,0.15) 100%
              ),
              linear-gradient(
                to top,
                #111 0%,
                transparent 50%
              ),
              url(${featuredMovie.backdrop_url})
            `,
          }}
        >

          <div className="hero-content">

            <p className="featured-label">
              FEATURED
            </p>

            <h1>
              {featuredMovie.title}
            </h1>

            <div className="hero-meta">

              <span>
                {featuredMovie.release_year}
              </span>

              <span>•</span>

              <span>
                {featuredMovie.rating} ⭐
              </span>

              <span>•</span>

              <span>
                {featuredMovie.duration} min
              </span>

            </div>

            <p className="hero-description">
              {featuredMovie.description}
            </p>

            <div className="hero-buttons">

              <button
                className="play-btn"
                onClick={() =>
                  openMovie(featuredMovie)
                }
              >
                ▶ Play
              </button>

              <button
                className="info-btn"
                onClick={() =>
                  openMovie(featuredMovie)
                }
              >
                ⓘ More Info
              </button>

            </div>

          </div>

        </section>

      )}


      {/* ================= CONTENT ================= */}

      {!search && (

        <main className="content">

          {loading && (
            <div className="loading">
              Loading Netflix...
            </div>
          )}

          {error && (
            <div className="error">
              {error}
            </div>
          )}

          {!loading && !error && (
            <>

              <MovieRow
                title="Trending Now"
                movies={trendingMovies}
                onMovieClick={openMovie}
              />

              <MovieRow
                title="Popular on Netflix"
                movies={movies}
                onMovieClick={openMovie}
              />

              <MovieRow
                title="Action & Adventure"
                movies={getByGenre("Action")}
                onMovieClick={openMovie}
              />

              <MovieRow
                title="Drama"
                movies={getByGenre("Drama")}
                onMovieClick={openMovie}
              />

              <MovieRow
                title="Comedy"
                movies={getByGenre("Comedy")}
                onMovieClick={openMovie}
              />

              <MovieRow
                title="Sci-Fi"
                movies={getByGenre("Sci-Fi")}
                onMovieClick={openMovie}
              />

            </>
          )}

        </main>

      )}


      {/* ================= MOVIE DETAILS MODAL ================= */}

      {selectedMovie && (

        <div
          className="modal-backdrop"
          onClick={closeMovie}
        >

          <div
            className="movie-modal"
            onClick={(e) =>
              e.stopPropagation()
            }
          >

            <button
              className="close-button"
              onClick={closeMovie}
            >
              ✕
            </button>

            <div
              className="modal-hero"
              style={{
                backgroundImage: `
                  linear-gradient(
                    to top,
                    #111 0%,
                    transparent 70%
                  ),
                  url(${selectedMovie.backdrop_url})
                `,
              }}
            />

            <div className="modal-content">

              <h1>
                {selectedMovie.title}
              </h1>

              <div className="modal-meta">

                <span>
                  {selectedMovie.release_year}
                </span>

                <span>
                  ⭐ {selectedMovie.rating}
                </span>

                <span>
                  {selectedMovie.duration} min
                </span>

              </div>

              <div className="modal-genres">

                {selectedMovie.genres?.map(
                  (genre) => (

                    <span key={genre.id}>
                      {genre.name}
                    </span>

                  )
                )}

              </div>

              <p className="modal-description">
                {selectedMovie.description}
              </p>

              <button className="modal-play">
                ▶ Play
              </button>

            </div>

          </div>

        </div>

      )}

    </div>
  );
}


/* ================= MOVIE ROW ================= */

function MovieRow({
  title,
  movies,
  onMovieClick,
}) {

  if (!movies || movies.length === 0) {
    return null;
  }

  return (

    <section className="movie-section">

      <h2>
        {title}
      </h2>

      <div className="movie-row">

        {movies.map((movie) => (

          <MovieCard
            key={movie.id}
            movie={movie}
            onClick={() =>
              onMovieClick(movie)
            }
          />

        ))}

      </div>

    </section>

  );
}


/* ================= MOVIE CARD ================= */

function MovieCard({
  movie,
  onClick,
}) {

  return (

    <div
      className="movie-card"
      onClick={onClick}
    >

      <img
        src={movie.poster_url}
        alt={movie.title}
      />

      <div className="movie-overlay">

        <h3>
          {movie.title}
        </h3>

        <div className="movie-info">

          <span>
            {movie.release_year}
          </span>

          <span>
            ⭐ {movie.rating}
          </span>

        </div>

      </div>

    </div>

  );
}


export default App;