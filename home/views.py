from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
import home.wayne as wayne

# Create your views here.

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
        
        # data = requests.get(f"https://api.themoviedb.org/3/search/tv?api_key={keys.MOVIE_API_KEY}&language=en-US&page=1&include_adult=false&query={query}")
        
        
        
        data = requests.get(f"https://api.themoviedb.org/3/search/{request.GET.get('type')}?api_key={wayne.MOVIE_API_KEY}&language=en-US&page=1&include_adult=false&query={query}")
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
    data = requests.get(f"https://api.themoviedb.org/3/tv/{tv_id}?api_key={wayne.MOVIE_API_KEY}&language=en-US")
    
    recommendations = requests.get(f"https://api.themoviedb.org/3/tv/{tv_id}/recommendations?api_key={wayne.MOVIE_API_KEY}&language=en-US")
    
    return render (request, 'tv_detail.html',{"data":data.json(), "recommendations":recommendations.json(), "type":"tv"})



def view_movie_detail(request, movie_id):
    data = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={wayne.MOVIE_API_KEY}&language=en-US")
    
    recommendations = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={wayne.MOVIE_API_KEY}&language=en-US")
    
    return render (request, 'movie_detail.html',{"data":data.json(), "recommendations":recommendations.json(),"type":"movie" })



def view_trendings_results(request):
    type = request.GET.get("media_type")
    time_window = request.GET.get("time_window")

    trendings = requests.get(f"https://api.themoviedb.org/3/trending/{type}/{time_window}?api_key={wayne.MOVIE_API_KEY}&language=en-US")
    return JsonResponse(trendings.json())



def comment_page(request,movie_id):
    if request.method == "POST":
        user = request.user
        comment = request.POST.get("comment")
        
        if not request.user.is_authenticated:
            user = User.objects.get(id=1)
            
        Comment(comment=comment, user=user, movie_id=movie_id).save()
        
        return redirect(f"/movie/{movie_id}/comments/")
        
    else:
        data = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={wayne.MOVIE_API_KEY}&language=en-US")
        
        title = data.json()["title"]
        
        comments = reversed(Comment.objects.filter(movie_id=movie_id))
        
        return render (request, "comments.html", {"title":title, "comments":comments})
