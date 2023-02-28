from django.http import Http404
from django.http import JsonResponse
from djangouploads.models import Movie
from django.shortcuts import render
from .serializers import Movieserilizer



def movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if movie is not None:
        return render(request, 'movies/movie.html', {'movie': movie})
    else:
        raise Http404('Movie does not exist')
    
# home page
def index(request):
    return render(request, 'index.html')

def movie_list(request):
    #get all the drinks
    # serialize them
    # return json
    movies = Movie.objects.all()
    serializer = Movieserilizer(movies, many=True)
    return JsonResponse({"movies": serializer.data}, safe=False)