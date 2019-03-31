#file in setting : SESSION_DATA
import pickle
import random

class DataManager():

    def __init__(self):
        self.position = [x, y]
        self.movieballs_nb = 0
        self.moviedex_moviemons = []
        self.moviemons = []

     def load(self, pickle_file):
        data_dict = {}
        try:
            with open(pickle_file+".pickle", "rb") as pickle_in:
                data_dict = pickle.load(pickle_in)
        except Exception as e:
            print(e)
            return (data_dict)
        return (data_dict)

     def dump(self, data_dict, pickle_file):
        try:
            with open(pickle_file+".pickle", 'wb') as pickle_out:
                pickle.dump(data_dict, pickle_out)
        except Exception as e:
            print(e)

     def get_random_movie(self):
        return (random.choice(list(self.moviemons.keys())))

#     def load_default_settings(self):
#       Charge les données de jeu dans l’instance de classe depuis
#       les settings. Requête et stocke les détails de tous les Moviemons sur IMDB. Retourne
#       l’instance courante.

#     def get_strength(self):
#       Retourne la force du joueur. (???? pas du film ???)

#     def get_movie(self):
#       Retourne un dictionnaire Python contenant tous les détails depuis le nom du Moviemon passé en paramètre et nécessaires à la page Detail.

def pickle_load(pickle_file):
    data_dict = {}
    try:
        with open(pickle_file+".pickle", "rb") as pickle_in:
            data_dict = pickle.load(pickle_in)
    except Exception as e:
        print(e)
        return (data_dict)
    return (data_dict)

def pickle_dump(data_dict, pickle_file):
    try:
        with open(pickle_file+".pickle", 'wb') as pickle_out:
            pickle.dump(data_dict, pickle_out)
    except Exception as e:
        print(e)

def get_random_movie(moviemons):
    return (random.choice(list(moviemons.keys())))

def main():
    example_dict = {1:"6",2:"2",3:"f"}
    pickle_dump(example_dict, "ex")
    dic = pickle_load("ex")
    print(dic)
    print(get_random_movie(example_dict))

if __name__ == '__main__':
    main()

