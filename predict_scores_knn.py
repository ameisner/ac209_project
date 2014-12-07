#!/usr/bin/env python

import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from load_reviews_scores import load_reviews_scores
import cPickle
from sklearn.feature_extraction.text import CountVectorizer

min_df_opt = 0.001 # from Naive Bayes cross-validation

# load review/score data (pass stem keyword along)
reviews, scores = load_reviews_scores()

# construct target vector
Y = (scores >= 7)

# load train/test indices
ind_train = cPickle.load(file('data/ind_train.pkl'))
ind_test = cPickle.load(file('data/ind_test.pkl'))

# make array of candidate min_df values
vectorizer = CountVectorizer(min_df=min_df_opt)
vectorizer.fit(reviews)
X = vectorizer.transform(reviews)

print X.shape

n_neighbors_list = [1, 2, 3, 4, 5, 10, 25, 50, 75, 100, 150, 200, 
                    250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]

rmse_values = np.zeros(len(n_neighbors_list))
for i, n_neighbors in enumerate(n_neighbors_list):
# all of the keyword inputs are defaults, except n_neighbors
    knnr = KNeighborsRegressor(n_neighbors=n_neighbors_list[i], weights='uniform', 
                               algorithm='auto', leaf_size=30, p=2, metric='minkowski', 
                               metric_params=None)

    knnr.fit(X[ind_train, :], scores[ind_train])
    pred = knnr.predict(X[ind_test, :])
    rmse_values[i] = np.std(pred-scores[ind_test])
    print i, n_neighbors_list[i], rmse_values[i]

o_rmse = open('data/knnr_rmse.pkl', 'wb')
cPickle.dump(rmse_values, o_rmse)
o_rmse.close()

o_nneighbor = open('data/knnr_nneighbor.pkl', 'wb')
cPickle.dump(n_neighbors_list, o_nneighbor)
o_nneighbor.close()
