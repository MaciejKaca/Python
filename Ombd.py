import omdb
import json
import operator

def search_movie(title):
    omdb.set_default('apikey', '463a3dd')
    res = omdb.title(title)
    #xml_content = res.content
    #movie = json.loads(xml_content)
    return (res)

def _input():
    movies = []
    user_input = ''
    while user_input != 'end':
        print(','.join(movies))
        user_input = input("Enter movie: ")

        type_sort=(user_input.split(':'))[-1]
        type_sort=type_sort.strip()

        if type_sort!="Rating" and type_sort!="Lenght" and type_sort!="Release date" and type_sort!="Popularity":
            if user_input != 'end':
                movies = (user_input.split(':'))[0]
                movies = movies.split(',')
                for movie in movies:
                    movie = movie.strip()
                    if movie in movies:
                        print("Some movies are repeated")
                    else:
                        movies.append(movie)
        else:
            if user_input != 'end':
                movies = (user_input.split(':'))[0]
                movies = movies.split(',')
                for movie in movies:
                    movie = movie.strip()
                    if movie in movies:
                        print("Some movies are repeated")
                    else:
                        movies.append(movie)
                        movies.append(type_sort)
    return movies

movies_sort = {}
movies = _input()

for movie in movies:
    if movies[-1] == 'Rating':
        movies_sort[movie] = (search_movie(movie))['imdb_rating']

sorted_x = sorted(movies_sort.items(), key=operator.itemgetter(1))

for x in sorted_x:
    print(search_movie(x[0]))