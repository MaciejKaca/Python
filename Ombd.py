import omdb
import json

def search_movie(title):
    omdb.set_default('apikey', '463a3dd')
    res = omdb.request(t=title)
    xml_content = res.content
    movie = json.loads(xml_content)
    print(json.dumps(movie, indent=4))

def _input():
    movies = []
    user_input = ''
    while user_input != 'end':
        print(','.join(movies))
        user_input = input("Enter movie: ")
        if user_input != 'end':
            for movie in user_input.split(',', len(user_input.split())):
                movie = movie.strip()
                if movie in movies:
                    print("Some movies are repeated")
                else:
                    movies.append(movie)
    return movies


movies = _input()
for movie in movies:
    search_movie(movie)