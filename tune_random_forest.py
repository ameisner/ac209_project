#!/usr/bin/env python
# written by Aaron Meisner, 12/6/2014

import cPickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import sklearn.grid_search
from load_reviews_scores import load_reviews_scores

def tune_random_forest(stem=False):
    min_df_opt = 0.001 # from Naive Bayes cross-validation

    # set up the list of trial n_trees values
    n_trees = np.array([1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 100, 150])

    # load review/score data (pass stem keyword along)
    reviews, scores = load_reviews_scores(stem=stem)

    # construct target vector
    Y = (scores >= 7)

    # load train/test indices
    ind_train = cPickle.load(file('data/ind_train.pkl'))

    # make array of candidate min_df values
    vectorizer = CountVectorizer(min_df=min_df_opt)
    vectorizer.fit(reviews)
    X = vectorizer.transform(reviews)

    print X.shape

    parameters = {'n_estimators' : n_trees}

    clf_gs = sklearn.grid_search.GridSearchCV(RandomForestClassifier(), 
                                              parameters, cv=10)
    clf_gs.fit(X[ind_train,:].toarray(), Y[ind_train])
    
    cv_means = np.array([clf_gs.grid_scores_[j][1] for j in range(len(n_trees))])
    cv_stds = np.array([np.std(clf_gs.grid_scores_[j][2]) for j in range(len(n_trees))])

    # write out results to pkl files
    o_ntree = open('data/rf_ntrees.pkl', 'wb')
    cPickle.dump(n_trees, o_ntree)
    o_ntree.close()

    o_score = open('data/rf_scores.pkl', 'wb')
    cPickle.dump(cv_means, o_score)
    o_score.close()

    o_std_score = open('data/rf_std_scores.pkl', 'wb')
    cPickle.dump(cv_stds, o_std_score)
    o_std_score.close()


