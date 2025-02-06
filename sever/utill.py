import warnings
warnings.filterwarnings('ignore')
import pickle

__movieList = None
__similarity = None
def load_saved_artifacts():
    global __movieList
    with open('./artifacts/movie_list.pickle''rb') as f:
        __movieList = pickle.loads(f)

    with open('./artifacts/similarity.pickle','rb') as f:
        __similarity = pickle.loads(f)

    print("Loading saved Artifacts Done")