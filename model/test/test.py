"""
Copyright (c) 2024 Tangtangfang Fang

All rights reserved.

This file is part of AVM-GRP.

AVM-GRP is distributed under the GPLv3 License.
See the LICENSE file at the top level of the distribution for details.
"""

import random
import joblib
import pandas as pd
import numpy as np
from model import Predictor
from Datasets.Data import Default, Default_Easy
import os


def FULL_TEST():
    df = pd.read_csv("./data/X_Full_test.csv")
    print(df.columns.tolist())
    predictor = Predictor.Predictor(X=df, model_sel='RF', lang=False)
    predicted_dict = predictor.Predict()
    High_err = list()
    if predicted_dict['status'] == 0:
        values = predicted_dict['values']
        y_df = pd.read_csv("./data/y_Full_test.csv")["price"].to_numpy()
        for i in range(len(y_df)):
            print(f'Predicted: {values[i]}, Actual: {y_df[i]}, Err: {np.abs(values[i] - y_df[i]): .1f}, Percent: {(np.abs(values[i] - y_df[i])) / y_df[i] * 100:.1f}')
            if (np.abs(values[i] - y_df[i])) / y_df[i] * 100 > 20.05:
                High_err.append(i)

        print(len(y_df))
        print(len(High_err))
    print(High_err)


def LOFI_TEST():
    df = pd.read_csv("./data/X_Easy_test.csv")
    print(df.columns.tolist())
    predictor = Predictor.Predictor(X=df, model_sel='RF', lang=False)
    predicted_dict = predictor.Predict()
    High_err = list()
    if predicted_dict['status'] == 0:
        values = predicted_dict['values']
        y_df = pd.read_csv("./data/y_Easy_test.csv")["price"].to_numpy()
        for i in range(len(y_df)):
            print(
                f'Predicted: {values[i]}, Actual: {y_df[i]}, Err: {np.abs(values[i] - y_df[i]): .1f}, Percent: {(np.abs(values[i] - y_df[i])) / y_df[i] * 100:.1f}')
            if (np.abs(values[i] - y_df[i])) / y_df[i] * 100 > 20.05:
                High_err.append(i)

        print(len(y_df))
        print(len(High_err))
    print(High_err)


def TEST():
    X_train, y_train, X_test, y_test = Default(os.path.dirname(__file__))
    predictor = Predictor.Predictor(X=X_train, model_sel='RF', lofi=False, lang=False)
    predicted_dict = predictor.Predict()
    High_err = list()
    if predicted_dict['status'] == 0:
        values = predicted_dict['values']
        y_df = y_train.to_numpy()
        for i in range(len(y_df)):
            print(
                f'Predicted: {values[i]}, Actual: {y_df[i]}, Err: {np.abs(values[i] - y_df[i]): .1f}, Percent: {(np.abs(values[i] - y_df[i])) / y_df[i] * 100:.1f}')
            if (np.abs(values[i] - y_df[i])) / y_df[i] * 100 > 20.05:
                High_err.append(i)

        print(len(y_df))
        print(len(High_err))
    print(High_err)


def CPTest(Full=True):
    if Full is True:
        X_train, y_train, X_test, y_test = Default(os.path.dirname(__file__))
    else:
        X_train, y_train, X_test, y_test = Default_Easy(os.path.dirname(__file__))
    X_valid = X_test.to_numpy()
    y_valid = y_test.to_numpy()
    predictor = Predictor.CpPredictor(X=None, full=Full, cwd=os.path.dirname(__file__))
    results = list()
    for k in range(100):
        i = random.randint(0, len(X_valid))
        predicted_dict = predictor.PredictByX(X_valid[i], ALPHA=0.5)
        print(f'value: {predicted_dict["values"]}, range: {predicted_dict["values_range"]}')
        results.append(f'value: {predicted_dict["values"]}, range: {predicted_dict["values_range"]}')


CPTest()
# Make(method='Easy')
# Make(method='Full')
