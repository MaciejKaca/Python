import os
import omdb
import json
from datetime import datetime

omdb.set_default('apikey', 'faaae6b8')
parameter=''

def search_movies(movies, _sorting_type):
     _movies = []
     for title in movies:
         res = omdb.request(t=title, r='json')
         data = json.loads(res.content)
         if 'Error' in data:
             print('Movie not found!')
         else:
             release_date = data['Released']
             objDate = datetime.strptime(release_date, '%d %b %Y')
             release_date = datetime.strftime(objDate, '%d-%m-%Y')
             popularity = int(data['imdbVotes'].replace(',', ''))
             length = int((data['Runtime'].split())[0])
             _movies.append({'Title': data['Title'], 'Release date': release_date, 'Rating': data['imdbRating'], 'Popularity' : popularity, 'Length' : length})

     if parameter != 'null':
         _movies = sorted(_movies, key=lambda k: k[_sorting_type], reverse=False)

     for movie in _movies:
        print(str(movie).replace("'", " "))

def sorting_type(user_input):
    sorting_type = user_input.split(' : ')
    if sorting_type[-1] == "Rating" or sorting_type[-1] == "Release date" or sorting_type[-1] == "Length" or sorting_type[-1] == "Popularity":
        return(sorting_type[-1])
    else:
        return 'null'

def movie_without_parameter(user_input):
    movie = user_input.split(' : ')
    return movie[0]


def input_movies():
    movies = []
    while(True):
        user_input = input('Movie title: ').split(', ')
        if(user_input[0] == 'end'):
            break
        for titles in user_input:
            movies.append(titles)
    return movies

movies_with_parameter = input_movies()
parameter = sorting_type(movies_with_parameter[-1])
movies = movies_with_parameter
movies[-1] = (movie_without_parameter(movies_with_parameter[-1]))

search_movies(movies, parameter)
