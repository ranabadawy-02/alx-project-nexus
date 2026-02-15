from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .tmdb_service import TMDbService

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def trending_view(request):
    """Get trending movies/TV shows"""
    media_type = request.GET.get('media_type', 'all')  # all, movie, tv
    time_window = request.GET.get('time_window', 'week')  # day, week
    page = request.GET.get('page', 1)
    
    data = TMDbService.get_trending(media_type, time_window, page)
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def discover_view(request):
    """Discover movies/TV shows with filters"""
    media_type = request.GET.get('media_type', 'movie')
    
    # Build filter parameters
    filters = {}
    
    if request.GET.get('genre'):
        filters['with_genres'] = request.GET.get('genre')
    
    if request.GET.get('sort_by'):
        filters['sort_by'] = request.GET.get('sort_by')
    
    if request.GET.get('year'):
        if media_type == 'movie':
            filters['primary_release_year'] = request.GET.get('year')
        else:
            filters['first_air_date_year'] = request.GET.get('year')
    
    if request.GET.get('rating_gte'):
        filters['vote_average.gte'] = request.GET.get('rating_gte')
    
    if request.GET.get('rating_lte'):
        filters['vote_average.lte'] = request.GET.get('rating_lte')
    
    if request.GET.get('page'):
        filters['page'] = request.GET.get('page')
    
    data = TMDbService.discover(media_type, **filters)
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_view(request):
    """Search for movies/TV shows"""
    query = request.GET.get('query', '')
    media_type = request.GET.get('media_type')  # movie, tv, or None for all
    page = request.GET.get('page', 1)
    
    if not query:
        return Response({'error': 'Query parameter is required'}, status=400)
    
    data = TMDbService.search(query, media_type, page)
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def genres_view(request):
    """Get list of genres"""
    media_type = request.GET.get('media_type', 'movie')
    data = TMDbService.get_genres(media_type)
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def details_view(request, media_type, media_id):
    """Get details for a specific movie/TV show"""
    data = TMDbService.get_details(media_type, media_id)
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def wizard_recommend_view(request):
    """Smart recommendation wizard based on user preferences"""
    media_type = request.GET.get('media_type', 'movie')
    if media_type == 'dontcare':
        media_type = 'movie'
    
    # Build filters based on wizard choices
    filters = {
        'sort_by': 'popularity.desc',
        'page': 1,
        'vote_count.gte': 100,  # At least 100 votes to filter out obscure content
    }
    
    # Mood -> Genres (more flexible)
    mood = request.GET.get('mood')
    if mood and mood != 'dontcare':
        mood_genres = {
            'dramatic': '18,28,12',  # Drama, Action, Adventure
            'intense': '53,80,27',  # Thriller, Crime, Horror
            'gentle': '35,10749,10751',  # Comedy, Romance, Family
            'curious': '99,36,9648',  # Documentary, History, Mystery
            'otherworldly': '878,14',  # Sci-Fi, Fantasy
            'realistic': '99,36'  # Documentary, History
        }
        if mood in mood_genres:
            filters['with_genres'] = mood_genres[mood]
    
    # Period -> Year range
    period = request.GET.get('period')
    if period and period != 'dontcare':
        from datetime import datetime
        current_year = datetime.now().year
        
        period_map = {
            'fresh': (current_year - 2, current_year),
            'recent': (current_year - 5, current_year),
            'modern': (current_year - 10, current_year),
            'golden': (2000, 2015),
            'throwback': (1990, 2000),
            'retro': (1900, 1990)
        }
        if period in period_map:
            year_range = period_map[period]
            if media_type == 'movie':
                filters['primary_release_date.gte'] = f'{year_range[0]}-01-01'
                filters['primary_release_date.lte'] = f'{year_range[1]}-12-31'
            else:
                filters['first_air_date.gte'] = f'{year_range[0]}-01-01'
                filters['first_air_date.lte'] = f'{year_range[1]}-12-31'
    
    # Quality -> Rating (more lenient)
    quality = request.GET.get('quality')
    if quality and quality != 'dontcare':
        quality_map = {
            'masterpiece': 7.5,  # Lowered from 8.0
            'high': 6.5,  # Lowered from 7.0
            'average': 5.0
        }
        if quality in quality_map:
            filters['vote_average.gte'] = quality_map[quality]
    
    # Runtime - REMOVED (TMDb Discover doesn't support runtime filtering well)
    # Popularity - Using vote_count instead
    popularity_level = request.GET.get('popularity')
    if popularity_level and popularity_level != 'dontcare':
        popularity_map = {
            'famous': 5000,  # Lowered from 50000
            'known': 1000,   # Lowered from 10000
            'hidden': 100
        }
        if popularity_level in popularity_map:
            filters['vote_count.gte'] = popularity_map[popularity_level]
    
    print(f"Wizard filters: {filters}")  # Debug print
    
    data = TMDbService.discover(media_type, **filters)
    
    print(f"Wizard results count: {len(data.get('results', [])) if data else 0}")  # Debug print
    
    return Response(data)