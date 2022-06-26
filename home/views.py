from django.shortcuts import render
import requests
from django.http import HttpResponse, JsonResponse

# Create your views here.
MOVIE_API_KEY = "05e5be7a518e07b0cdd93bf0e133083a"

def search(request):
    
    '''
    Get the query from the search box
    '''
    query = request.GET.get('q')
    print(query)
    
    '''
    If the query is not empty
    '''
    if query:
        
        # data = requests.get(f"https://api.themoviedb.org/3/search/tv?api_key={MOVIE_API_KEY}&language=en-US&page=1&include_adult=true&query={query}")
        
        
        data = requests.get(f"https://api.themoviedb.org/3/search/{request.GET.get('type')}?api_key={MOVIE_API_KEY}&language=en-US&page=1&include_adult=true&query={query}")
        '''
        Looking for the response of the request we use (data.json()) or (data.text)
        '''
        print(data.json())
        # print(data.text)
            
            
    else:
        return HttpResponse("Please enter a search query")
    
    
    
    
    
    return render(request, 'results.html',{"data":data.json(),"type": request.GET.get("type")})

def index(request):
    return render (request, "index.html")

# https://api.themoviedb.org/3/search/tv?api_key=03401687fc726546579b53d2f0d65ee7&language=en-US&page=1&include_adult=false&query=batman


def view_tv_detail(request, tv_id):
    data = requests.get(f"https://api.themoviedb.org/3/tv/{tv_id}?api_key={MOVIE_API_KEY}&language=en-US")
    
    return render (request, 'tv_detail.html',{"data":data.json()})
