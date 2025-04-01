# -*- coding: utf-8 -*-
"""course work.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XxLU4epsr26i7PXHoGeVSpGLcbxCrfNl

3. Tune the hyperparameters and build the most accurate model
"""

from sklearn.model_selection import GridSearchCV,RepeatedKFold,RandomizedSearchCV

"""For Linear Regression"""

model = LinearRegression()
cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
space = dict()
space['fit_intercept'] = [True, False]
space['normalize'] = [True, False]
space['copy_X'] = [True, False]
search = GridSearchCV(model, space, scoring='neg_mean_absolute_error', n_jobs=1, cv=cv)
result = search.fit(x_train, y_train)
print('Best Score: %s' % result.best_score_)
print('Best Hyperparameters: %s' % result.best_params_)
print('LinearRegression GridSearch Accuracy: %s' % result.best_estimator_.score(x_test,y_test))

"""Accurate model:"""

linearRegressor = LinearRegression(normalize=True,fit_intercept=False,copy_X=True)
linearRegressor.fit(x_train, y_train)
yPrediction = linearRegressor.predict(x_test)
print("RMSE score:",np.sqrt(mean_squared_error(y_test,yPrediction)))
print("R2 score:",r2_score(y_test,yPrediction))

"""For Lasso Regression"""

model = Lasso()
cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
space = dict()
space['alpha'] = [1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 100]
space['fit_intercept'] = [True, False]
space['normalize'] = [True, False]
space['max_iter'] = [1,10,50,100]
space['copy_X'] = [True, False]
space['warm_start'] = [True, False]
space['selection'] = ['cyclic', 'random']
space['precompute'] = [True, False,]
search = GridSearchCV(model, space, scoring='neg_mean_absolute_error', n_jobs=-1, cv=cv)
result = search.fit(x_train, y_train)

print('Best Score: %s' % result.best_score_)
print('Best Hyperparameters: %s' % result.best_params_)
print('Lasso GridSearch Accuracy: %s' % result.best_estimator_.score(x_test,y_test))

"""Accurate Model:"""

model_lasso = Lasso(alpha=0.01,selection='random')
model_lasso.fit(x_train, y_train)
pred_lasso= model_lasso.predict(x_test)
print("RMSE score:",np.sqrt(mean_squared_error(y_test,pred_lasso)))
print("R2 score:",r2_score(y_test, pred_lasso))

"""For Ridge Regression"""

model = Ridge()
cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
space = dict()
space['solver'] =  ['svd', 'cholesky', 'lsqr', 'sparse_cg', 'sag', 'saga']
space['alpha'] = [1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 100]
space['fit_intercept'] = [True, False]
space['normalize'] = [True, False]
space['max_iter'] = [1,10,50,100,500,1000]
space['copy_X'] = [True, False]
search = GridSearchCV(model, space, scoring='neg_mean_absolute_error', n_jobs=-1, cv=cv)
result = search.fit(x_train, y_train)

print('Best Score: %s' % result.best_score_)
print('Best Hyperparameters: %s' % result.best_params_)
print('Ridge GridSearch Accuracy: %s' % result.best_estimator_.score(x_test,y_test))

"""Accurate Model:"""

rr = Ridge(alpha=1,solver = 'lsqr')
rr.fit(x_train, y_train)
pred_rr= rr.predict(x_test)
print("RMSE score:",np.sqrt(mean_squared_error(y_test,pred_rr)))
print("R2 score:",r2_score(y_test, pred_rr))

"""For Nearest Neighbour Regression"""

model=neighbors.KNeighborsRegressor()

leaf_size = list(range(1,50))
n_neighbors = list(range(1,30))
p=[1,2]
hyperparameters = dict(leaf_size=leaf_size, n_neighbors=n_neighbors, p=p)

search = GridSearchCV(model, hyperparameters, cv=10)
result = search.fit(x_train, y_train)

print('Best Score: %s' % result.best_score_)
print('Best Hyperparameters: %s' % result.best_params_)
print('Knn GridSearch Score: %s' % result.best_estimator_.score(x_test,y_test))

"""Accurate Model:"""

model = neighbors.KNeighborsRegressor(n_neighbors = 16,algorithm='kd_tree',p=1,weights='distance')
model.fit(x_train, y_train)  #fit the model
pred_knn=model.predict(x_test) #make prediction on test set
error = sqrt(mean_squared_error(y_test,pred_knn)) #calculate rmse

print('RMSE value :', error)
print("R2 score:",r2_score(y_test, pred_knn))

"""For Support Vector Regression"""

model = SVR()
cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
space = dict()
space['max_iter'] = [1,10,50,100]
space['kernel']= ['linear','poly','rbf','sigmoid']
space['gamma'] = [1, 0.1, 0.01, 0.001, 0.0001]
space['C']: [0.1, 1, 10, 100, 1000]

search = GridSearchCV(model, space, scoring='neg_mean_absolute_error', n_jobs=-1, cv=cv)

result = search.fit(x_train, y_train)

print('Best Score: %s' % result.best_score_)
print('Best Hyperparameters: %s' % result.best_params_)
print('SVR GridSearch Accuracy: %s' % result.best_estimator_.score(x_test,y_test))

"""Accurate Model:"""

'''
SVR()
SupportVectorReg=SVR(kernel='poly',gamma=1)
SupportVectorReg.fit(x_train,y_train)
pred_svr=SupportVectorReg.predict(x_test)

print("MSE score:",np.sqrt(mean_squared_error(y_test,pred_svr)))
print("R2 score:",r2_score(y_test, pred_svr))
'''
SupportVectorReg=SVR()
SupportVectorReg.fit(x_train,y_train)
pred_SVR=SupportVectorReg.predict(x_test)
print("MSE score:",np.sqrt(mean_squared_error(y_test,pred_SVR)))
print("R2 score:",r2_score(y_test, pred_SVR))

"""For Tree Regression"""

model = DecisionTreeRegressor()
cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
space = dict()
space['max_depth']= [None,1,2,3,4,5,6,7]
space['max_features']= [None, 'sqrt', 'auto', 'log2', 0.3,0.5,0.7 ]
space['min_samples_split']= [2,0.3,0.5]
space['min_samples_leaf']=[1, 0.3,0.5]
space['criterion'] = ['mse','friedman_mse','mae']
space['splitter'] = ['best','random']
search = GridSearchCV(model, space, scoring='neg_mean_absolute_error', n_jobs=-1, cv=cv)
result = search.fit(x_train, y_train)
print('Best Score: %s' % result.best_score_)
print('Best Hyperparameters: %s' % result.best_params_)

"""Accurate Model:"""

DecisionTreeReg=DecisionTreeRegressor(criterion= 'friedman_mse', max_depth= 6, max_features= 'auto', min_samples_leaf= 1, min_samples_split= 2, splitter= 'random')
DecisionTreeReg.fit(x_train,y_train)
pred_tree=DecisionTreeReg.predict(x_test)
print("RMSE score:",np.sqrt(mean_squared_error(y_test,pred_tree)))
print("R2 score:",r2_score(y_test, pred_tree))

"""For Random Forest Regression"""

model = RandomForestRegressor()
n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]
max_features = ['auto', 'sqrt','log2']
max_depth = [int(x) for x in np.linspace(10, 1000,10)]

min_samples_split = [2, 5, 10,14]
min_samples_leaf = [1, 2, 4,6,8]

random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf
              }

RF_RandomCv = RandomizedSearchCV(estimator=model,param_distributions=random_grid,n_iter=100,cv=3,verbose=2,
                               random_state=100,n_jobs=-1)
result=RF_RandomCv.fit(x_train,y_train)

print('Best Score: %s' % result.best_score_)
print('Best Hyperparameters: %s' % result.best_params_)
print('Random Forest GridSearch Accuracy: %s' % result.best_estimator_.score(x_test,y_test))

"""Accurate Model:"""

RandomForestReg=RandomForestRegressor(max_depth=8, max_features='sqrt',n_estimators=200)
RandomForestReg.fit(x_train,y_train)
pred_forest=RandomForestReg.predict(x_test)
print("RMSE score:",np.sqrt(mean_squared_error(y_test,pred_forest)))
print("R2 score:",r2_score(y_test, pred_forest))

"""For Gradient Boosted Regression"""

model =GradientBoostingRegressor()
cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
space = dict()
space['n_estimators']= [200, 500]
space['max_features']= ['auto', 'sqrt', 'log2']
space['max_depth'] = [4,5,6,7,8]
space['alpha'] = [1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 100,0.99]
space['loss'] = ['ls', 'lad', 'huber', 'quantile']
space['subsample'] = [1]
search = RandomizedSearchCV(model, space, scoring='neg_mean_absolute_error', n_jobs=-1, cv=cv)
result = search.fit(x_train, y_train)
print('Best Score: %s' % result.best_score_)
print('Best Hyperparameters: %s' % result.best_params_)

"""Accurate Model:"""

regressor = GradientBoostingRegressor(
    subsample =  1,
    n_estimators= 500,
    max_features= 'log2',
    max_depth= 5,
    loss= 'lad',
    alpha= 0.01
)
regressor.fit(x_train,y_train)
pred_gboost = regressor.predict(x_test)
print("RMSE score:",np.sqrt(mean_squared_error(y_test,pred_gboost)))
print("R2 score:",r2_score(y_test,pred_gboost))