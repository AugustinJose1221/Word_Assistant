from gensim.models import Word2Vec
import multiprocessing
loaded_model = Word2Vec.load('model.bin')
def Target_Word(context_words_list):
    target_words = loaded_model.predict_output_word(context_words_list, topn=10)  #Predicting context words for the list of target words
    return target_words

