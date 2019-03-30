#file in setting : SESSION_DATA
import pickle


class DataManager():

    def __init__(self):
        #self.position = [x, y]
        #self.movieballs_nb = 0
        #self.moviedex_moviemons = []
        #self.moviemons = []

     def load(self, pickle_file):
        data_dict = {}
        try:
            with open(pickle_file, "rb") as pickle_in:
                data_dict = picke.load(pickle_in)
        except:
            print("Error : Could not load pickle file !")
            return (data_dict)
         return (data_dict)

     def dump(self, data_dict, pickle_file):
        with open(pickle_file, 'wb') as pickle_out:
            pickle.dump(data_dict, pickle_out)

     def get_random_movie(self):

#     def load_default_settings(self):
    
#     def get_strength(self):

#     def get_movie(self):



def main():

pickle_out = open("dict.pickle","wb")
pickle.dump(example_dict, pickle_out)
if __name__ == '__main__':
    main()
