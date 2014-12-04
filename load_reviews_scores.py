# written by Aaron Meisner, 12/4/2014

import json
import numpy as np
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer

def remove_empty_reviews(rev_list, scores):
    l = np.array([len(r.replace(' ', '')) for r in rev_list])

    return rev_list[l > 0], scores[l > 0]

def load_reviews_scores(stem=False):
    f = open('data/gamespot.json')
    data = json.load(f)

    rev_list = np.array([g['summary'] for g in data])
    scores = np.array([g['score'] for g in data]).astype(float)

    rev_list, scores = remove_empty_reviews(rev_list, scores)

    u, ind_u = np.unique(rev_list, return_index=True)
    rev_list = rev_list[ind_u]
    scores = scores[ind_u]

    if stem:
        stemmer = PorterStemmer()
        rev_list_stemmed = []
        tokenizer = RegexpTokenizer(ur'\b[a-zA-Z][a-zA-Z]+\b')

        for rev in rev_list:
            tokens = tokenizer.tokenize(rev)
            stemmed = ""
            for token in tokens:
                stemmed = stemmed + " " + stemmer.stem(token)
            rev_list_stemmed.append(stemmed)
        return rev_list_stemmed, scores
    else:
        return rev_list, scores
