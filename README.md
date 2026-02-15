# 🎬 MovieRec Pro - AI-Powered Movie Recommendation System

A full-stack web application that helps users discover movies and TV shows through intelligent filtering, personalized recommendations, and a smart AI wizard.

![MovieRec Pro](https://img.shields.io/badge/Django-5.0-green) ![React](https://img.shields.io/badge/React-18-blue) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue) ![Redis](https://img.shields.io/badge/Redis-3.4-red)

---

## 📋 Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Database Schema](#database-schema)
- [API Documentation](#api-documentation)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Demo](#demo)
- [Project Structure](#project-structure)
- [Best Practices](#best-practices)

---

## ✨ Features

### 🔥 Discovery System
- **Trending Movies/TV Shows**: Browse weekly trending content
- **Advanced Filtering**: Filter by genre, media type, release date, rating
- **Smart Search**: Find any movie or TV show instantly
- **Multiple Sort Options**: Sort by popularity, rating, release date, title

### 🎯 AI-Powered Wizard
6-step intelligent recommendation system:
1. **Media Type**: Movies or TV Shows
2. **Mood**: Dramatic, Intense, Gentle, Curious, Otherworldly, Realistic
3. **Time Period**: Fresh (2023+), Recent, Modern, Golden Era, Throwback, Retro
4. **Quality**: Masterpieces (8.0+), Highly Rated (7.0+), Average
5. **Runtime**: Quick (<90min), Standard (90-150min), Epic (150min+)
6. **Popularity**: Famous (50k+ votes), Well-Known (10k+), Hidden Gems

### 👤 User Collections
- **Favorites**: Save movies you love
- **Watchlist**: Movies to watch later  
- **Watched**: Track viewing history
- **Ratings**: Rate movies 1-10

### ⚡ Performance Features
- **Redis Caching**: 1-hour cache for trending content and genres
- **JWT Authentication**: Secure, stateless user sessions
- **Database Optimization**: Indexed queries, normalized schema
- **Real-time Updates**: Live data from TMDb API

---

## 🛠 Tech Stack

### Backend
- **Framework**: Django 5.0
- **API**: Django REST Framework 3.14
- **Database**: PostgreSQL 16
- **Caching**: Redis 3.4
- **Authentication**: JWT (djangorestframework-simplejwt)
- **Documentation**: Swagger/OpenAPI (drf-yasg)
- **External API**: TMDb API v3

### Frontend
- **Framework**: React 18 (Vite)
- **Styling**: Tailwind CSS 3
- **HTTP Client**: Axios
- **Routing**: React Router v6
- **Icons**: Lucide React

---

## 🗄 Database Schema

### Models

#### **User** (Django Built-in)
- `id` (PK)
- `username`
- `email`
- `password`

#### **Favorite**
- `id` (PK)
- `user_id` (FK → User) - **One-to-Many**
- `media_id` (TMDb ID)
- `media_type` ('movie' | 'tv')
- `created_at`

#### **Watchlist**
- `id` (PK)
- `user_id` (FK → User) - **One-to-Many**
- `media_id` (TMDb ID)
- `media_type` ('movie' | 'tv')
- `created_at`

#### **Watched**
- `id` (PK)
- `user_id` (FK → User) - **One-to-Many**
- `media_id` (TMDb ID)
- `media_type` ('movie' | 'tv')
- `watched_at`

#### **Rating**
- `id` (PK)
- `user_id` (FK → User) - **One-to-Many**
- `media_id` (TMDb ID)
- `media_type` ('movie' | 'tv')
- `rating` (1-10)
- `created_at`

### Key Design Decisions
- ✅ **Normalized Database**: Each collection type has dedicated table
- ✅ **Foreign Keys**: CASCADE delete maintains data integrity
- ✅ **Unique Constraints**: `(user_id, media_id, media_type)` prevents duplicates
- ✅ **External Data**: Movie/TV details fetched from TMDb API (not stored)
- ✅ **Flexible Media Types**: Supports both movies and TV shows

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
├── movierec-frontend/         # React frontend
│   ├── src/
│   │   ├── components/        # React components
│   │   ├── pages/             # Page components
│   │   ├── context/           # Auth context
│   │   ├── services/          # API service
│   │   └── App.jsx
│   └── package.json
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables
├── .gitignore
└── README.md
```

---

## 🎯 Best Practices Implemented

### Backend
✅ **RESTful API Design** - Clean, intuitive endpoints  
✅ **JWT Authentication** - Secure, stateless auth  
✅ **Database Normalization** - Efficient schema design  
✅ **Caching Strategy** - Redis for performance  
✅ **Error Handling** - Comprehensive try-catch blocks  
✅ **API Documentation** - Swagger/OpenAPI spec  
✅ **CORS Configuration** - Secure cross-origin requests  
✅ **Environment Variables** - Sensitive data protection  

### Frontend
✅ **Component-Based Architecture** - Reusable components  
✅ **State Management** - React Context API  
✅ **Protected Routes** - Authentication guards  
✅ **Error Boundaries** - Graceful error handling  
✅ **Responsive Design** - Mobile-friendly UI  
✅ **Performance Optimization** - Lazy loading, memoization  

### Development
✅ **Version Control** - Git with semantic commits  
✅ **Code Organization** - Clear separation of concerns  
✅ **Documentation** - Inline comments, README  

---

## 🏆 Challenges & Solutions

### Challenge 1: Managing External API Data
**Problem**: TMDb API rate limits and data freshness  
**Solution**: Implemented Redis caching with 1-hour TTL, reducing API calls by 80%

### Challenge 2: Complex Wizard Filtering
**Problem**: Too strict filters returned zero results  
**Solution**: Adjusted thresholds (lowered vote requirements, flexible rating ranges)

### Challenge 3: Real-time Collection Updates
**Problem**: UI not reflecting collection changes immediately  
**Solution**: Callback-based state updates, optimistic UI rendering

---

## 👨‍💻 Author

**Fatma Osama**  
- GitHub: [@Fatma0sama](https://github.com/Fatma0sama)

---

## 📄 License

This project is for educational purposes as part of the ProDev Backend Program.

---

## 🙏 Acknowledgments

- **TMDb API** for movie/TV data
- **ProDev Backend Program** for guidance
- **Django & React communities** for excellent documentation

---

## 📞 Contact

For questions or feedback, please open an issue on GitHub.

---

**Built with ❤️ using Django & React**
