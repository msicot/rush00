import requests


def get_monster_movies():
    API_KEY = "27f3beda"
    s = requests.session()
    URL = "http://www.omdbapi.com/?apikey=" + API_KEY + "&t="
    movie_list = ["alien", "black sheep", "godzilla", "jurassic park", "dinoshark", "sharktopus",
                  "Mega Shark vs. Crocosaurus", "Jurassic shark", "anaconda", "Attack of the Crab Monsters",
                  "Mega Piranha", "Jaws", "Cloverfield", "Pacific Rim", "Trollhunter"]
    moviemon_db = []
    for movie in movie_list:
        d = s.get(url=URL + movie).json()
        moviemon_db.append(d)
    return moviemon_db


if __name__ == "__main__":
    moviemons = get_monster_movies()
    for each in moviemons:
        print(each)
    pass
