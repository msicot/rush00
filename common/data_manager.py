# file in setting : SESSION_DATA
from django.conf import settings
import pickle
import random
import os
import datetime
from .moviemon import get_monster_movies


random.seed(datetime.datetime.now())


def pickle_load(pickle_file):
    data_dict = {}
    try:
        with open(pickle_file, "rb") as pickle_in:
            data_dict = pickle.load(pickle_in)
    except Exception as e:
        print(e)
        return (data_dict)
    return (data_dict)


def pickle_dump(data_dict, pickle_file):
    try:
        with open(pickle_file, 'wb') as pickle_out:
            pickle.dump(data_dict, pickle_out)
    except Exception as e:
        print(e)


def get_random_movie(moviemons):
    return (random.choice(list(moviemons.keys())))


class DataManager:

    def __init__(self, filename):
        self.filename = filename
               # self.position = [x, y]
               # self.movieballs_nb = 0
               # self.moviedex_moviemons = []
               # self.moviemons = []

    def load(self, filename=None):
        if filename == None:
            filename = self.filename
            return (pickle_load(filename))

    def dump(self, game_log):
        save_file = os.listdir('common/save_folder/')
        if self.filename.count('/') == 2:
            for elem in save_file:
                if elem[:5] == self.filename.split('/')[2][:5]:
                    os.remove('common/save_folder/' + elem)
        pickle_dump(game_log, self.filename)
        return None

    def get_random_movie(self, moviemon_db):
        movie_index = random.randint(0, len(moviemon_db) - 1)
        return {**moviemon_db[movie_index]}

    def load_default_settings(self):
        if os.path.isfile(self.filename):
            os.remove(self.filename)
            game_log = {
                'size': settings.GAME_CONFIG['size'],
                    'first_position': settings.GAME_CONFIG['first_position'],
                    'current_position': 0,
                    'x': 0,
                    'y': 0,
                    'scale': '',
                    'event': '',
                    'movieball': 100,
                    'start': False,
                    'moviemon_db': get_monster_movies(),
                    'moviemon_db2': get_monster_movies(),
                    'captured_moviemon': [],
                    'captured_moviemon_nb': 0,
                    'moviemon_found': None
                }
            pickle_dump(game_log, self.filename)

    def get_strength(self, data):
        return len(data['captured_moviemon'])
    """Retourne la force du joueur. (???? pas du film ???)"""

    def get_movie(self, data):
        movies = self.load("common/game.log")
        for movie in movies['moviemon_db']:
            if movie.get('Title') == data:
                return movie
        return None


if __name__ == '__main__':

    pass
