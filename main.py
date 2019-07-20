import func
import json
import matplotlib.pyplot as plt

name = input("Input the moive you are looking for:")
js = func.get_movies_from_tastedive(name)
titles = func.extract_movie_titles(js)
mv_list = func.get_related_titles(titles)

mv_data = [func.get_movie_data(mv) for mv in mv_list]
rate_lab = func.ex_ratemd(mv_data)



print(" ")
print("---------------------------")
print("The rating source for the recommended movies are:")
for source in rate_lab:
    print(source)

print("---------------------------")

source = input("Pick a ranking source in list above for recommendation..")
rate_lst = func.get_movie_rating(mv_data, source)


print(" ")
print("The detail ratings:")

print("---------------------------")

for key in rate_lst.keys():
    print("{}: {}".format(key,rate_lst[key]))




print("---------------------------")

print(" ")

rank_lst = func.sorted_mv(rate_lst)

print('The recommended movies are listed from highest score to lowest as following:')
count = 0
print("---------------------------")

for mv in rank_lst:
    count += 1
    print('{} {}'.format(count, mv))
#print(func.get_movie_rating(func.get_movie_data(name)))
