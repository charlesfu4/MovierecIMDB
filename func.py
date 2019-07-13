import requests_with_caching
import json

def get_movies_from_tastedive(name):
    baseurl = "https://tastedive.com/api/similar"
    param_dict = {}
    param_dict['q'] = name
    param_dict['type'] = "movies"
    param_dict['limit'] = 5
    res = requests_with_caching.get(baseurl, params = param_dict)
    print(res.url)
    return res.json()

def extract_movie_titles(js):
    title = []
    for i in range(len(js['Similar']['Results'])):
        title.append(js['Similar']['Results'][i]['Name'])
    return title

def get_related_titles(lst):
    mv_lst = []
    for title in lst:
        temp = extract_movie_titles(get_movies_from_tastedive(title))
        for movie in temp:
            if movie not in mv_lst:
                mv_lst.append(movie)
    return mv_lst


