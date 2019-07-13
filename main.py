import func
import json


name = input("Please enter movie name:")
print(func.get_movie_rating(func.get_movie_data(name)))
