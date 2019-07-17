import requests
import json

def get_movies_from_tastedive(name):
    baseurl = "https://tastedive.com/api/similar"
    param_dict = {}
    param_dict['k'] = '340176-movierec-3PBXNWIB'
    param_dict['q'] = name
    param_dict['type'] = "movie"
    param_dict['limit'] = 3
    res = requests.get(baseurl, params = param_dict)
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

def get_movie_data(name):
    baseurl = "http://www.omdbapi.com/"
    param_dict = {}
    param_dict['apikey'] = "d0ba26e6"
    param_dict['t'] = name
    param_dict['r'] = "json"
    res = requests.get(baseurl, param_dict)
    return res.json()


def get_movie_rating(mvdatalst):
    rate = {}
    for mvdata in mvdatalst:
        for dic in mvdata['Ratings']:
            if("Rotten Tomatoes" in dic.values()):
                rate[mvdata['Title']] = int(dic['Value'][:-1])
                break
            else:
                rate[mvdata['Title']] = 0
        
    return rate
            

def sorted_mv(rate):
    s_lst = sorted(rate, key = lambda x : (rate[x],x), reverse = True)

    return s_lst

