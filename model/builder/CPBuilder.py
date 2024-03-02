import random

from mapie.regression import MapieRegressor
from sklearn.ensemble import RandomForestRegressor
import joblib
from Datasets.Data import Default, Default_Easy
import os
from model.Predictor import Predictor
import pandas as pd


def numpy2df(numpy_arr, full):
    if full is True:
        feature_name = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view',
                        'condition',
                        'grade',
                        'sqft_above', 'sqft_basement', 'building_age', 'renovated_year', 'lat', 'long',
                        'sqft_living15',
                        'sqft_lot15', 'year', 'month']
    else:
        feature_name = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'building_age', 'lat', 'long']
    df = pd.DataFrame([numpy_arr])
    df.columns = feature_name
    return df


def check():
    X_train, y_train, X_test, y_test = Default(os.path.dirname(__file__))
    rf = joblib.load('../object/RF_Full.mdo')
    mapie_rf = MapieRegressor(estimator=rf, n_jobs=-1, verbose=0, cv='prefit')
    mapie_rf.fit(X_test, y_test)
    mapie_pred, mapie_pis = mapie_rf.predict(X_test, alpha=0.2)
    print(mapie_pis)
    print(mapie_pred)
    joblib.dump(mapie_rf, 'mapie_rf.mdo')


def Make(method):
    if method == 'Full':
        X_train, y_train, X_test, y_test = Default(os.path.dirname(__file__))
        rf = joblib.load('../object/RF_Full.mdo')
    elif method == 'Easy':
        X_train, y_train, X_test, y_test = Default_Easy(os.path.dirname(__file__))
        rf = joblib.load('../object/RF_Easy.mdo')
    else:
        X_train, y_train, X_test, y_test = Default(os.path.dirname(__file__))
        rf = joblib.load('../object/RF_Full.mdo')
    mapie_rf = MapieRegressor(estimator=rf, n_jobs=-1, verbose=0, cv='prefit')
    mapie_rf.fit(X_test, y_test)
    mapie_pred, mapie_pis = mapie_rf.predict(X_test, alpha=0.2)
    print(mapie_pis)
    print(mapie_pred)
    joblib.dump(mapie_rf, f'MAPIE_{method}.mdo')
    print(f'MAPIE_{method}.mdo saved successfully')


def compare(iters):
    _, _, X_test, y_test = Default(os.path.dirname(__file__))
    X_test_numpy = X_test.to_numpy()
    y_test_numpy = y_test.to_numpy()
    mapie_rf = joblib.load('mapie_rf.mdo')
    count = 0
    err_list = list()
    for i in range(iters):
        mapie_pred, mapie_pis = mapie_rf.predict(numpy2df(X_test_numpy[i], True), alpha=0.2)
        predictor = Predictor(X_test_numpy[i], model_sel='RF', full=True, lang=False, cwd=os.path.dirname(__file__))
        pred_price = predictor.Predict()
        print(f"RF: {pred_price['values'][0]}, CP: {mapie_pred[0]}, True: {y_test_numpy[i]}")
        pred_range = [mapie_pis[0][0][0], mapie_pis[0][1][0]]
        if y_test_numpy[i] < pred_range[0] or y_test_numpy[i] > pred_range[1]:
            count = count + 1
            err_list.append(f"CP: {pred_range[0]} - {pred_range[1]}, True: {y_test_numpy[i]}")

    print(count)
    for i in err_list:
        print(i)


def Test(method='Full', iters=100, train=True):
    if method == 'Full':
        X_train, y_train, X_test, y_test = Default(os.path.dirname(__file__))
        rf = joblib.load('../object/RF_Full.mdo')
        mapie_rf = joblib.load('../object/MAPIE_Full.mdo')
        full = True
    elif method == 'Easy':
        X_train, y_train, X_test, y_test = Default_Easy(os.path.dirname(__file__))
        rf = joblib.load('../object/RF_Easy.mdo')
        mapie_rf = joblib.load('../object/MAPIE_Easy.mdo')
        full = False
    else:
        X_train, y_train, X_test, y_test = Default(os.path.dirname(__file__))
        rf = joblib.load('../object/RF_Full.mdo')
        mapie_rf = joblib.load('../object/MAPIE_Full.mdo')
        full = True
    if train is True:
        X_valid = X_train.to_numpy()
        y_valid = y_train.to_numpy()
    else:
        X_valid = X_test.to_numpy()
        y_valid = y_test.to_numpy()
    print(type(mapie_rf))
    count = 0
    err_list = list()
    for k in range(iters):
        i = random.randint(0, X_valid.shape[0] - 1)
        mapie_pred, mapie_pis = mapie_rf.predict(numpy2df(X_valid[i], full), alpha=0.2)
        pred_price = rf.predict(numpy2df(X_valid[i], full))
        print(f"RF: {pred_price[0]}, CP: {mapie_pred[0]}, True: {y_valid[i]}")
        pred_range = [mapie_pis[0][0][0], mapie_pis[0][1][0]]
        if y_valid[i] < pred_range[0] or y_valid[i] > pred_range[1]:
            count = count + 1
            err_list.append(f"RF: {pred_price[0]}, CP: {pred_range[0]} - {pred_range[1]}, True: {y_valid[i]}")

    print(count)
    for i in err_list:
        print(i)




# check()
# compare(iters=100)
# Make(method='Easy')
# Make(method='Full')
Test(method='Full', iters=1, train=True)

