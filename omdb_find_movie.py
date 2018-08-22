import os
import omdb
import json
from datetime import datetime

omdb.set_default('apikey', 'faaae6b8')

def movies_from_folder():
    path = 'C:\Movies'

    list_for_erase = ['5.1', '7.1', '5 1', '7 1', 'DUAL AUDIO', 'DUAL-AUDIO', 'MULTI-CHANNEL', 'Ita-Eng',
                      '2160p', '4K', '1080p', '720p', '480p', '360p', 'HD', 'FULL HD', 'FULLHD',
                      'x264', 'CH', 'X264', 'HEVC', 'WEB-DL', 'BrRip', 'Rip', 'DVDRip', 'XviD', 'BLURAY',
                      'EXTENDED', 'REMASTERED', 'DIRECTORS', 'UNRATED', 'AlTERNATE', 'DVD']

    files = []
    clear_files = []
    for file in os.listdir(path):
        files.append(file)

    for title in files:
        for word in list_for_erase:
            title = title.replace(word, "")
        title = os.path.splitext(title)[0]
        clear_files.append(title.strip())

    return clear_files

def search_movies(movies, parameter):
     movies_to_seach = []
     for title in movies:
         res = omdb.request(t=title, r='json')
         data = json.loads(res.content)
         if 'Error' in data:
             print('Movie not found!')
         else:
             release_date = data['Released']
             objDate = datetime.strptime(release_date, '%d %b %Y')
             release_date = datetime.strftime(objDate, '%d.%m.%Y')
             popularity = int(data['imdbVotes'].replace(',', ''))
             length = int((data['Runtime'].split())[0])
             movies_to_seach.append({'Title': data['Title'], 'Release date': release_date, 'Rating': data['imdbRating'], 'Popularity' : popularity, 'Length' : length})

     if parameter != 'null':
         movies_to_seach = sorted(movies_to_seach, key=lambda k: k[parameter], reverse=False)

     for movie in movies_to_seach:
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

def input_decision():
    while (True):
        user_input = input('Manual / Folder? [M] or [F]: ')
        if (user_input == 'F'):
            return 'F'
        if (user_input == 'M'):
            return  'M'

if input_decision() == 'M':
    movies_with_parameter = input_movies()
    parameter = sorting_type(movies_with_parameter[-1])
    movies = movies_with_parameter
    movies[-1] = (movie_without_parameter(movies_with_parameter[-1]))
else:
    movies = movies_from_folder()
    parameter = 'null'

search_movies(movies, parameter)