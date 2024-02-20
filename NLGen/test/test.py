import joblib
from Datasets.Data import Default
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


def FULL_TEST():
    X_train, y_train, X_test, y_test = Default(os.path.dirname(__file__))
    kmeans = joblib.load('../class/kmeans_model_Full.mdo')
    avg = joblib.load('../class/class_avg_Full.mdo')
    X_train_numpy = X_train.to_numpy()
    df = numpy2df(X_train_numpy[0], full=True)
    pred = kmeans.predict(df)[0]
    avg_pred = avg[pred]
    print(f"Predict class: {pred}")
    print(f"Values: {df.to_numpy()[0].tolist()}")
    print(f"Class avg: {avg_pred}")


FULL_TEST()
