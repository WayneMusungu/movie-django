from django.shortcuts import render
import requests
from django.http import HttpResponse

# Create your views here.
TMDB_API_KEY = "05e5be7a518e07b0cdd93bf0e133083a"

def search(request):
    
    results = []
    query = request.GET.get('q')
    if query:
        print("1")
        data = requests.get(f"https://api.themoviedb.org/3/search/tv?api_key={TMDB_API_KEY}&language=en-US&page=1&include_adult=false&query={query}")
        # print(data.json())
        
        # temp = []
        # for m in data.json() ["results"]:
        #     if len(temp) < 6 :
                
        #         temp.append({"poster_path":m["poster_path"],"name":m["name"],"origin_country":m["origin_country"],"original_name":m["original_name"],"overview":m["overview"],"popularity": m["popularity"]})
        #     else:
        #         results.append(temp)
                
        #     results.append(temp) if len(temp) > 0 else None
            
    else:
        return HttpResponse("Please enter a search query")
    
    
    
    return render(request, 'results.html',{"data":data.json()})

def index(request):
    return render (request, "index.html")

