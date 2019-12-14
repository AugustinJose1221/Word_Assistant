from nltk.corpus import brown
from gensim.models import Word2Vec
import multiprocessing

sentences= brown.sents()
EMB_DIM = 300
w2v = Word2Vec(sentences, size = EMB_DIM, window = 5, min_count = 5, negative = 15, iter = 10, workers = multiprocessing.cpu_count())
w2v.save('model.bin')
