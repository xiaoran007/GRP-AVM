from mapie.regression import MapieRegressor
from sklearn.ensemble import RandomForestRegressor
import joblib
from Datasets.Data import Default, Default_Easy
import os
from model.Predictor import Predictor
import pandas as pd


def Make(method):
    if method == 'Full':
        X_train, y_train, X_test, y_test = Default(os.path.dirname(__file__))
    elif method == 'Easy':
        X_train, y_train, X_test, y_test = Default_Easy(os.path.dirname(__file__))
    else:
        X_train, y_train, X_test, y_test = Default(os.path.dirname(__file__))
    rf = RandomForestRegressor(n_jobs=-1, criterion='squared_error', verbose=0)
    rf.fit(X=X_train, y=y_train)
    joblib.dump(rf, f'RF_{method}.mdo')




Make(method='Easy')
