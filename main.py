import func
import json
name1 = input("Input the moive you are looking for:")
js = func.get_movies_from_tastedive(name1)
titles = func.extract_movie_titles(js)
mv_list = func.get_related_titles(titles)
print(mv_list)
#name2 = input("Please enter movie name:")
#print(func.get_movie_rating(func.get_movie_data(name)))
