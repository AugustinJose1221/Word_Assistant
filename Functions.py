from gensim.models import Word2Vec
import multiprocessing
import string
loaded_model = Word2Vec.load('model.bin')
def Target_Word(context_words_list):
    target_words = loaded_model.predict_output_word(context_words_list, topn=10)  #Predicting context words for the list of target words
    return target_words
def Word_List(sentence):
    words = sentence.split()
    string_map = str.maketrans('', '', string.punctuation)
    word_list = [w.translate(string_map) for w in words]
    return word_list
def Suggestions(sequence):
    words = []
    for i in sequence:
        words.append(i[0])
    return words
        





