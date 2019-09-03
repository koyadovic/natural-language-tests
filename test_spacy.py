import spacy


# we have
# spacy.load('en_core_web_sm')
# spacy.load("xx_ent_wiki_sm")
# spacy.load("es_core_news_sm")

# TODO read this:
# https://towardsdatascience.com/custom-named-entity-recognition-using-spacy-7140ebbb3718

nlp = spacy.load("es_core_news_sm")


text = ''''''


doc = nlp(text)
for token in doc:
    print(token.text, token.pos_, token.dep_)
