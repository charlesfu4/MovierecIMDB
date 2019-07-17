import func
import json

name = input("Input the moive you are looking for:")
js = func.get_movies_from_tastedive(name)
titles = func.extract_movie_titles(js)
mv_list = func.get_related_titles(titles)

mv_data = [func.get_movie_data(mv) for mv in mv_list]
#print(json.dumps(mv_data, indent = 2))
rate_lst = func.get_movie_rating(mv_data)
print(rate_lst)
rank_lst = func.sorted_mv(rate_lst)
print('The recommended movies are listed from highest score to lowest as following:')
count = 0
for mv in rank_lst:
    count += 1
    print('{} {}'.format(count, mv))
#print(func.get_movie_rating(func.get_movie_data(name)))
