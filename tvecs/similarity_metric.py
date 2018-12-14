from tvecs.bilingual_generator import bilingual_generator as bg
from tvecs.vector_space_mapper import vector_space_mapper as vm
from gensim.models import KeyedVectors

import os

train_bilingual_corpus = 'data/bilingual_dictionary/en-fr.txt'
test_bilingual_corpus = 'data/bilingual_dictionary/en-fr.txt'

bilingual_dict = bg.load_bilingual_dictionary(train_bilingual_corpus)

vector_space_mapper = vm.VectorSpaceMapper(
    model_1=KeyedVectors.load_word2vec_format('data/models/t-vex-english-fb-model')
        ,
    model_2=KeyedVectors.load_word2vec_format('data/models/t-vex-french-model') #change
        ,
    bilingual_dict=bilingual_dict
)

vector_space_mapper.map_vector_spaces()

print("Training MSE: {} %".format(vector_space_mapper.obtain_mean_square_error_from_dataset(
    dataset_path=train_bilingual_corpus
)))

print("Testing MSE: {} %".format(vector_space_mapper.obtain_mean_square_error_from_dataset(
    dataset_path=test_bilingual_corpus
)))

word1 = raw_input("Please input the english word :")
word2 = raw_input("Please input another english word :")

trans1 = vector_space_mapper.get_recommendations_from_word(word1.lower(), topn=1, pretty_print=False)[0][0]
trans2 = vector_space_mapper.get_recommendations_from_word(word2.lower(), topn=1, pretty_print=False)[0][0]

distance_1 = vector_space_mapper.get_cosine_similarty_same_lang(word1,word2,'en')
distance_2 = vector_space_mapper.get_cosine_similarty_same_lang(trans1,trans2,'hn')

print "English words :", word1, word2, " Distance metric :", distance_1
print "Hindi translations obtained from model :", trans1, trans2
print "Distance between them :", distance_2