# file in setting : SESSION_DATA
from django.conf import settings
import pickle
import random
import os
from .moviemon import get_monster_movies


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


class DataManager():

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
            'movieball': 0,
            'start': False,
            'moviemon_db': get_monster_movies(),
            'captured_moviemon': [],
			'captured_moviemon_nb': 0,
            'moviemon_found': None
        }
        pickle_dump(game_log, self.filename)

    def get_strength(self):
        pass
        """Retourne la force du joueur. (???? pas du film ???)"""

    def get_movie(self):
        pass
        """ 
    Retourne un dictionnaire Python contenant tous les détails depuis le nom du Moviemon passé en paramètre 
    et nécessaires à la page Detail.
    """


def main():
    example_dict = {1: "6", 2: "2", 3: "f"}
    pickle_dump(example_dict, "ex")
    dic = pickle_load("ex")
    print(dic)
    print(get_random_movie(example_dict))


if __name__ == '__main__':

    main()
