Source Repository:
https://github.com/KshitijKarthick/tvecs

Pretrained Word vectors downloaded from  :
https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md
Note --- We have not included the pre-trained word vectors of embedding size 300 of the languages -
English, Hindi, Bengali, Tamil as each of these is of size 3.3 GB and it was getting difficult to upload the code of such a huge size.
Before running, kindly download the word vectors and place it in the data/models directly with
naming convention as t-vex-<Language name>-model


[1]Prerequisites

-  Python 2.7 setup and installed
-  Pip setup and installed (pip install -r requirements.txt)
-  Ensure all dependencies of requirements.txt are satisfied
-  Download nltk_data using nltk.download() -> only tokenizers required
-  Download corpus and extract in specified directory
-  Setup the basic development environment from the source repository [python setup.py install]


[2]Data
The following sources were used to generate bilingual dictionary for three language
    - Emille Corpora http://www.emille.lancs.ac.uk/
    - Leipzig Corpora http://corpora.uni-leipzig.de/
The corpus is not added in the file as those were huge files of around 3GB


Files Created:
1. Bilingual Dictionary
We have generated Bilingual dictionary from Yandex API for English-French, English-Bengali, English-Tamil
2. word_synonyms_bengali.py, word_synonyms_french.py, word_synonyms_hindi.py, word_synonyms_tamil.py
These scripts find the most similar words in target language for a word given in source language.
3. similarity_metric.py
This is the script written to find the cosine distance between similar synonyms across different language vector spaces.


Files  Modified:
1. vector_space_mapper.py
--Implemented the function get_cosine_similarty_same_lang to compute cosine similarity between two words
--Implemented logic to handle unseen words
2. main.py
--Imported KeyedVectors from gensim.models to read the pre-trained word vectors from Facebook. For this use gensim version 3.2.0
3.bilingual_generator.py
--Changed logic to read the training corpus
4.requirements.txt
--Updated the version of gensim package to 3.2.0

Files Added:
In Models directory, added pre-trained word vectors in english, french, tamil and bengali released by Facebook
You need not use the training corpus as the models have already been generated.

Commands:

[1]To get most similar words in target language for a given source word in english language:
python
   python tvecs/word_synonyms_french.py
   python tvecs/word_synonyms_hindi.py
   python tvecs/word_synonyms_tamil.py
   python tvecs/word_synonyms_bengali.py

[2] To get the cosine distance between similar synonyms across different language vector spaces:
    python similarity_metric.py

[3] To compute the reduction in mean squared error:

    python -im tvecs -l1 english -l2 <Target language> -m1 ./data/models/t-vex-english-fb-model -m2 ./data/models/<Target Language Model> -b ./data/bilingual_dictionary/<Bilingual File Name>

    #Sample Output

    Enter your Choice:
    1> Recommendation
    2> Exit

    Choice: 1
    Enter word in Language english: examination

    Word    =>  Score

    जाँच    =>  0.643208742142
    नियुक्ति    =>  0.640852451324
    जांच    =>  0.638412773609
    अध्ययन  =>  0.638307392597
    विवेचना =>  0.638229370117
    मंत्रणा =>  0.634038448334
    पुनर्मूल्यांकन  =>  0.627283990383
    अध्‍ययन =>  0.624040842056
    निरीक्षण    =>  0.623490035534
    जाच =>  0.619904220104