# 🎬 MovieRec Pro - AI-Powered Movie Recommendation Backend

A robust backend system for managing users, movie/TV collections, and AI-powered recommendations. Built for scalability, performance, and secure RESTful APIs.


---

## 📋 Contents
  •	Features￼
	•	Backend Requirements￼
	•	Database Schema￼
	•	API Documentation￼
	•	Installation￼
	•	Environment Variables￼
	•	Usage￼
	•	Project Structure￼
	•	Best Practices￼
	•	Author￼
	•	License￼
	•	Acknowledgments￼
	•	Contact￼

---
✨ Features

🔹 User Management
	•	Register and authenticate users with JWT tokens
	•	Retrieve and update user profiles
	•	Secure, stateless sessions

🔹 Movie/TV Collections
	•	Favorites: Save movies/TV shows users love
	•	Watchlist: Track movies to watch later
	•	Watched: Maintain viewing history
	•	Ratings: Rate movies or TV shows (1–10)

🔹 AI-Powered Recommendation Wizard
	•	6-step intelligent recommendation engine
	•	Filters include media type, mood, era, quality, runtime, popularity
	•	Personalized recommendations based on user selections

🔹 Performance & Optimization
	•	Redis caching for trending movies/genres (1-hour TTL)
	•	Indexed queries and normalized database schema
	•	Real-time integration with TMDb API

⸻

🛠 Backend Requirements

System
	•	Python 3.10+
	•	PostgreSQL 16
	•	Redis 3.4+
	•	TMDb API key

Python Dependencies
	•	Django 5.0
	•	Django REST Framework 3.14
	•	djangorestframework-simplejwt
	•	drf-yasg (Swagger/OpenAPI)
	•	psycopg2-binary (PostgreSQL connector)
	•	redis (Python client)

All dependencies are listed in requirements.txt.

⸻

🗄 Database Schema

Models

User (Django Built-in)
	•	id (PK)
	•	username
	•	email
	•	password

Favorite
	•	id (PK)
	•	user_id (FK → User) - One-to-Many
	•	media_id (TMDb ID)
	•	media_type (‘movie’ | ‘tv’)
	•	created_at

Watchlist
	•	id (PK)
	•	user_id (FK → User) - One-to-Many
	•	media_id (TMDb ID)
	•	media_type (‘movie’ | ‘tv’)
	•	created_at

Watched
	•	id (PK)
	•	user_id (FK → User) - One-to-Many
	•	media_id (TMDb ID)
	•	media_type (‘movie’ | ‘tv’)
	•	watched_at

Rating
	•	id (PK)
	•	user_id (FK → User) - One-to-Many
	•	media_id (TMDb ID)
	•	media_type (‘movie’ | ‘tv’)
	•	rating (1–10)
	•	created_at

Key Design Decisions
	•	✅ Normalized schema for efficiency
	•	✅ Foreign keys with CASCADE delete for integrity
	•	✅ Unique constraints (user_id, media_id, media_type)
	•	✅ External data fetched from TMDb API only

---

## 📡 API Documentation

### Authentication Endpoints
```
POST   /api/auth/register/     - Create new user account
POST   /api/auth/login/        - Login and get JWT tokens
GET    /api/auth/profile/      - Get current user profile
```

### Movie Endpoints
```
GET    /api/movies/trending/            - Get trending movies/TV
GET    /api/movies/discover/            - Discover with filters
GET    /api/movies/search/              - Search movies/TV
GET    /api/movies/genres/              - Get genre list
GET    /api/movies/details/{type}/{id}/ - Get movie/TV details
GET    /api/movies/wizard/recommend/    - AI wizard recommendations
```

### Collection Endpoints
```
GET    /api/auth/favorites/      - List user favorites
POST   /api/auth/favorites/      - Add to favorites
DELETE /api/auth/favorites/{id}/ - Remove from favorites

GET    /api/auth/watchlist/      - List watchlist
POST   /api/auth/watchlist/      - Add to watchlist
DELETE /api/auth/watchlist/{id}/ - Remove from watchlist

GET    /api/auth/watched/        - List watched movies
POST   /api/auth/watched/        - Mark as watched
DELETE /api/auth/watched/{id}/   - Unmark as watched

GET    /api/auth/ratings/        - List user ratings
POST   /api/auth/ratings/        - Rate a movie/TV
PUT    /api/auth/ratings/{id}/   - Update rating
```

**Full API Documentation**: `http://localhost:8000/api/docs/` (Swagger UI)

---

## 🚀 Installation

### Prerequisites
- Python 3.10+
- Node.js 18+
- PostgreSQL 16
- Redis 3.4+
- TMDb API Key ([Get it here](https://www.themoviedb.org/settings/api))

### Backend Setup

1. **Clone the repository**
```bash
git clone https://github.com/Fatma0sama/movierec-backend.git
cd movierec-backend
```

2. **Create virtual environment**
```bash
python -m venv venv
# Windows:
.\venv\Scripts\Activate
# Mac/Linux:
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
Create `.env` file:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=movierec_db
DB_USER=movierec_user
DB_PASSWORD=movierec123
DB_HOST=localhost
DB_PORT=5432
TMDB_API_KEY=your-tmdb-api-key
ALLOWED_HOSTS=localhost,127.0.0.1
REDIS_LOCATION=redis://127.0.0.1:6379/1
```

5. **Create PostgreSQL database**
```bash
psql -U postgres
CREATE DATABASE movierec_db;
CREATE USER movierec_user WITH PASSWORD 'movierec123';
GRANT ALL PRIVILEGES ON DATABASE movierec_db TO movierec_user;
\q
```

6. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

7. **Start Redis**
```bash
redis-server
```

8. **Run development server**
```bash
python manage.py runserver
```

Backend runs at: `http://127.0.0.1:8000`

---

### Frontend Setup

1. **Navigate to frontend directory**
```bash
cd movierec-frontend
```

2. **Install dependencies**
```bash
npm install
```

3. **Start development server**
```bash
npm run dev
```

Frontend runs at: `http://localhost:5173`

---

## 🔐 Environment Variables

### Backend (.env)
| Variable | Description | Example |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | `django-insecure-xxx` |
| `DEBUG` | Debug mode | `True` |
| `DB_NAME` | Database name | `movierec_db` |
| `DB_USER` | Database user | `movierec_user` |
| `DB_PASSWORD` | Database password | `movierec123` |
| `DB_HOST` | Database host | `localhost` |
| `DB_PORT` | Database port | `5432` |
| `TMDB_API_KEY` | TMDb API key | `your-api-key` |
| `REDIS_LOCATION` | Redis connection | `redis://127.0.0.1:6379/1` |

---

## 💻 Usage

1. **Register an account** at `http://localhost:5173/register`
2. **Login** with your credentials
3. **Browse trending** movies and TV shows
4. **Use filters** to discover content by genre, type, rating
5. **Try the AI Wizard** - Click "Surprise Me" for personalized recommendations
6. **Save content** to Favorites or Watchlist
7. **Rate movies** 1-10 to track your preferences

---

## 🎥 Demo

- **Demo Video**: [Link to YouTube/Google Drive]
- **Live API Documentation**: [Swagger UI Link]
- **Presentation**: [Google Slides Link]

---

## 📁 Project Structure
```
MovieRecPro/
├── movierec_backend/          # Django backend
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL config
│   └── wsgi.py
├── accounts/                  # User & collections app
│   ├── models.py              # Favorite, Watchlist, Watched, Rating
│   ├── views.py               # API views
│   ├── serializers.py         # DRF serializers
│   └── urls.py
├── movies/                    # Movies app
│   ├── views.py               # Movie endpoints
│   ├── tmdb_service.py        # TMDb API integration
│   └── urls.py
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables
├── .gitignore
└── README.md
```

---

## 🏆 Best Practices Implemented

	•	RESTful API design, JWT auth
	•	Database normalization, indexing, unique constraints
	•	Redis caching for performance
	•	Error handling and logging
	•	Swagger/OpenAPI documentation

---

## 👨‍💻 Author

**Rana Mohsen**  
- GitHub: [@Fatma0sama](https://github.com/ranabadawy_02)

---

## 📄 License

for educational purposes as part of the ProDev Backend Program.


---

## 📞 Contact

For questions or feedback, please open an issue on GitHub.


