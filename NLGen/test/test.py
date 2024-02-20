import joblib
from Datasets.Data import Default, Default_Easy
import os
import pandas as pd


def numpy2df(numpy_arr, full):
    if full is True:
        feature_name = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view', 'condition',
                        'grade',
                        'sqft_above', 'sqft_basement', 'building_age', 'renovated_year', 'lat', 'long', 'sqft_living15',
                        'sqft_lot15', 'year', 'month']
    else:
        feature_name = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'building_age', 'lat', 'long']
    df = pd.DataFrame([numpy_arr])
    df.columns = feature_name
    return df


def EASY_TEST():
    X_train, y_train, X_test, y_test = Default_Easy(os.path.dirname(__file__))
    kmeans = joblib.load('../class/kmeans_model_Easy.mdo')
    avg = joblib.load('../class/class_avg_Easy.mdo')
    X_train_numpy = X_train.to_numpy()
    df = numpy2df(X_train_numpy[0], full=False)
    pred = kmeans.predict(df)[0]
    avg_pred_X = avg[pred][0]
    avg_pred_price = avg[pred][1]
    print(f"Predict class: {pred}")
    print(f"Values: {df.to_numpy()[0].tolist()}")
    print(f"Class avg: {avg_pred_X}")
    print(f"Price avg: {avg_pred_price}")


def FULL_TEST():
    X_train, y_train, X_test, y_test = Default(os.path.dirname(__file__))
    kmeans = joblib.load('../class/kmeans_model_Full.mdo')
    avg = joblib.load('../class/class_avg_Full.mdo')
    X_train_numpy = X_train.to_numpy()
    df = numpy2df(X_train_numpy[0], full=True)
    pred = kmeans.predict(df)[0]
    avg_pred_X = avg[pred][0]
    avg_pred_price = avg[pred][1]
    print(f"Predict class: {pred}")
    print(f"Values: {df.to_numpy()[0].tolist()}")
    print(f"Class avg: {avg_pred_X}")
    print(f"Price avg: {avg_pred_price}")


def TEST():
    avg = joblib.load('../class/class_avg_Full.mdo')
    for i, j in avg.items():
        print(f"{i}: {j[1]}")


TEST()
