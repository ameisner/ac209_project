# written by Aaron Meisner, 5/12/2014

import cPickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import sklearn.grid_search
from load_reviews_scores import load_reviews_scores

def crossval_naive_bayes(stem=False, regex=False):
    # load review/score data (pass stem keyword along)
    # construct Y

    reviews, scores = load_reviews_scores(stem=stem)
    Y = (scores >= 7)

    #     load train/test indices

    ind_train = cPickle.load(file('data/ind_train.pkl'))

    # make array of candidate min_df values
    min_dfs = np.array([0.00008, 0.0001, 0.0005, 0.001, 0.002, 
                        0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009,
                        0.01])

    min_dfs = np.arange(0.00008, 0.01002, 0.00002)
    # make array of candidate alpha values
    alphas = np.array([0.005, 0.1, 0.5, 1, 2, 5, 10])

    n_min_df = len(min_dfs)
    n_alpha = len(alphas)

    # initialize 2d grid of cv scores
    grid_cv_score = np.zeros((n_min_df, n_alpha))
    grid_min_df = np.zeros((n_min_df, n_alpha))
    grid_alpha = np.zeros((n_min_df, n_alpha))

    # initialize 2d grid of min_df values
    # initialize 2d grid of alpha values

    parameters = {'alpha' : alphas}

    for i, min_df in enumerate(min_dfs):
    #     print out parameter values
        print i, min_df
    #     construct X 
        vectorizer = CountVectorizer(min_df=min_df)
        vectorizer.fit(reviews)
        X = vectorizer.transform(reviews)
  
    #     restrict to the train indices
        clf_gs = sklearn.grid_search.GridSearchCV(MultinomialNB(), parameters,
                                                   cv=10)
        clf_gs.fit(X[ind_train,:], Y[ind_train])
        clf_gs.grid_scores_

    #     run 10 fold CV with gridsearch
        cv_means = np.array([clf_gs.grid_scores_[j][1] for j in range(n_alpha)])
    #     store the cross validation scores in 2d grid
        grid_cv_score[i, :] = cv_means
        grid_min_df[i, :] = min_df
        grid_alpha[i, :] = alphas

    # write out 2d grids to pkl file
    o_scores = open('data/grid_cv_score.pkl', 'wb')
    cPickle.dump(grid_cv_score, o_scores)
    o_scores.close()

    o_alphas = open('data/grid_alpha.pkl', 'wb')
    cPickle.dump(grid_alpha, o_alphas)
    o_alphas.close()

    o_min_dfs = open('data/grid_min_df.pkl', 'wb')
    cPickle.dump(grid_min_df, o_min_dfs)
    o_min_dfs.close()
