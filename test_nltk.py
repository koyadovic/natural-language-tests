import nltk


# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')


def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent


text = '''Esto es una prueba de texto. Mañana quizá me acerque a la biblioteca. Bueno, me despido, adios.'''

pattern = 'NP: {<DT>?<JJ>*<NN>}'
cp = nltk.RegexpParser(pattern)

sent = preprocess(text)
cs = cp.parse(sent)
print(cs)



