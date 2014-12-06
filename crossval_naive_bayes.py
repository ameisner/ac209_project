#!/usr/bin/env python
# written by Aaron Meisner, 5/12/2014

import cPickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import sklearn.grid_search
from load_reviews_scores import load_reviews_scores

def crossval_naive_bayes(stem=False, regex=False):
    # load review/score data (pass stem keyword along)
    reviews, scores = load_reviews_scores(stem=stem)

    # construct target vector
    Y = (scores >= 7)

    # load train/test indices
    ind_train = cPickle.load(file('data/ind_train.pkl'))

    # make array of candidate min_df values
    min_dfs = np.arange(0.00008, 0.01002, 0.00002)
    # make array of candidate alpha values
    alphas = np.array([0.005, 0.1, 0.5, 1, 1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3, 5, 
                       10])

    n_min_df = len(min_dfs)
    n_alpha = len(alphas)

    # initialize 2d grids holding cross-validation results
    grid_cv_score = np.zeros((n_min_df, n_alpha))
    grid_score_std = np.zeros((n_min_df, n_alpha))
    grid_min_df = np.zeros((n_min_df, n_alpha))
    grid_alpha = np.zeros((n_min_df, n_alpha))

    parameters = {'alpha' : alphas}

    for i, min_df in enumerate(min_dfs):
    #   print out current min_df parameter value
        print i, min_df
    #   construct feature matrix 
        vectorizer = CountVectorizer(min_df=min_df)
        vectorizer.fit(reviews)
        X = vectorizer.transform(reviews)
  
    #   restrict to the training indices and run 10-fold CV with GridSearchCV
        clf_gs = sklearn.grid_search.GridSearchCV(MultinomialNB(), parameters,
                                                   cv=10)
        clf_gs.fit(X[ind_train,:], Y[ind_train])
        clf_gs.grid_scores_

        cv_means = np.array([clf_gs.grid_scores_[j][1] for j in range(n_alpha)])
        cv_stds = np.array([np.std(clf_gs.grid_scores_[j][2]) for j in range(n_alpha)])
    #   store information about inputs and scores for this value of min_df
        grid_cv_score[i, :] = cv_means
        grid_score_std[i, :] = cv_stds
        grid_min_df[i, :] = min_df
        grid_alpha[i, :] = alphas

    # write out 2d grids to pkl file
    o_scores = open('data/grid_cv_score.pkl', 'wb')
    cPickle.dump(grid_cv_score, o_scores)
    o_scores.close()

    o_score_stds = open('data/grid_score_std.pkl', 'wb')
    cPickle.dump(grid_score_std, o_score_stds)
    o_score_stds.close()

    o_alphas = open('data/grid_alpha.pkl', 'wb')
    cPickle.dump(grid_alpha, o_alphas)
    o_alphas.close()

    o_min_dfs = open('data/grid_min_df.pkl', 'wb')
    cPickle.dump(grid_min_df, o_min_dfs)
    o_min_dfs.close()
