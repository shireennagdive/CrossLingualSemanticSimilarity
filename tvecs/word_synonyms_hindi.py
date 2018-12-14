from tvecs.bilingual_generator import bilingual_generator as bg
from tvecs.vector_space_mapper import vector_space_mapper as vm
from gensim.models import Word2Vec
import os

# train_bilingual_corpus = 'data/bilingual_dictionary/en-fr.txt'
# test_bilingual_corpus = 'data/bilingual_dictionary/en-fr.txt'
#
bilingual_dict = bg.load_bilingual_dictionary('data/bilingual_dictionary/english_hindi_bd')

vector_space_mapper = vm.VectorSpaceMapper(
    model_1=Word2Vec.load(
            os.path.join('data', 'models', 't-vex-english-model')
        ),
    model_2=Word2Vec.load(
        os.path.join('data', 'models', 't-vex-hindi-model')),
    bilingual_dict=bilingual_dict
)


vector_space_mapper.map_vector_spaces()

# print("Training MSE: {} %".format(vector_space_mapper.obtain_mean_square_error_from_dataset(
#     dataset_path=train_bilingual_corpus
# )))
#
# print("Testing MSE: {} %".format(vector_space_mapper.obtain_mean_square_error_from_dataset(
#     dataset_path=test_bilingual_corpus
# )))

word = raw_input("Please input the english word :")

while word != '///':
    print vector_space_mapper.get_recommendations_from_word(
        word.lower(),
        pretty_print=True
    )
    word = raw_input("Please input the english word :")

