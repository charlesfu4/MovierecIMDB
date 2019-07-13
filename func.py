import requests
import json

def get_movies_from_tastedive(name):
    baseurl = "https://tastedive.com/api/similar"
    param_dict = {}
    param_dict['q'] = name
    param_dict['type'] = "movies"
    param_dict['limit'] = 5
    res = requests.get(baseurl, params = param_dict)
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

def get_movie_data(name):
    baseurl = "http://www.omdbapi.com/"
    param_dict = {}
    param_dict['apikey'] = "d0ba26e6"
    param_dict['t'] = name
    param_dict['r'] = "json"
    res = requests.get(baseurl, param_dict)
    return res.json()


def get_movie_rating(js):
    rate_s = ""
    for dic in js['Ratings']:
        if("Rotten Tomatoes" in dic.values()):
            rate_s = dic['Value']
    if rate_s == "":
        rate = 0
        return rate
    rate = int(rate_s[:-1])
    return rate

def get_sorted_recommendations(title_lst):
    g_lst = get_related_titles(title_lst)
    dic_m_r = {}
    for name in g_lst:
        if(name not in dic_m_r):
            dic_m_r[name] = get_movie_rating(get_movie_data(name))
    s_lst = sorted(dic_m_r, key = lambda x : (dic_m_r[x],x), reverse = True)

    return s_lst

