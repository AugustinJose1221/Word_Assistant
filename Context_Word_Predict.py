from gensim.models import Word2Vec
import multiprocessing
loaded_model = Word2Vec.load('model.bin')
context_words_list = ['He','went','to','get','a']
target_words = loaded_model.predict_output_word(context_words_list, topn=10)  #Predicting context words for the list of target words

