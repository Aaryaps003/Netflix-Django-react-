# 🎬 Netflix Clone — React + Django

A full-stack Netflix-inspired web application built using **React.js** and **Django REST Framework**.

The project demonstrates frontend development, REST API integration, database management, JWT authentication, movie search, movie details, and user-specific "My List" functionality.

---

## 🚀 Features

### 🎥 Movie Management
- Movie database using Django models
- Genre management
- Movie posters and backdrop images
- Featured movies
- Trending movies
- Movie ratings and release information

### 🖥️ Netflix-Style Frontend
- Netflix-inspired dark UI
- Responsive navigation bar
- Hero banner
- Horizontal movie rows
- Movie cards with hover effects
- Responsive design for different screen sizes

### 🔍 Search
- Search movies by title
- Dynamic search results
- No page reload required

### ℹ️ Movie Details
- Movie backdrop
- Description
- Rating
- Release year
- Duration
- Genres
- Movie information modal

### 🔐 Authentication
- User registration
- JWT-based login
- JWT access and refresh tokens
- Protected API endpoints

### ❤️ My List
- Add movies to personal list
- Remove movies from personal list
- User-specific movie lists
- Duplicate movie prevention

---

## 🛠️ Technology Stack

### Frontend

- React.js
- Vite
- Axios
- HTML5
- CSS3

### Backend

- Python
- Django
- Django REST Framework
- Simple JWT
- django-cors-headers

### Database

- SQLite

### Development Tools

- Git
- GitHub
- Postman
- VS Code

---

## 🏗️ Project Architecture

```text
                React Frontend
                      │
                      │ HTTP / REST API
                      ▼
              Django REST Framework
                      │
          ┌───────────┴───────────┐
          │                       │
       Movies API             Auth API
          │                       │
          ▼                       ▼
      Movie Data              JWT Auth
          │
          ▼
        SQLite
          │
          ▼
       My List
