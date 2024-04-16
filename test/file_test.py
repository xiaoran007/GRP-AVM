"""
Copyright (c) 2024 Tangtangfang Fang

All rights reserved.

This file is part of AVM-GRP.

AVM-GRP is distributed under the GPLv3 License.
See the LICENSE file at the top level of the distribution for details.
"""

import os

from Datasets.Data import Default, Default_Easy
from model.Predictor import CpPredictor
import pandas as pd

"""
    This file is not final test file.
"""


def genExample(full=True):
    cp_predictor = CpPredictor(X=None, cwd=os.path.dirname(__file__), full=full, alpha=0.2)
    if full:
        X_train, y_train, X_test, y_test = Default(os.path.dirname(__file__))
        file_name_no_price = 'resources/Full_example_OpenDay_NoPrice.csv'
        file_name = 'resources/Full_example_OpenDay.csv'
    else:
        X_train, y_train, X_test, y_test = Default_Easy(os.path.dirname(__file__))
        file_name_no_price = 'resources/Easy_example_OpenDay_NoPrice.csv'
        file_name = 'resources/Easy_example_OpenDay.csv'
    X = X_train
    X_numpy = X.to_numpy()
    y = y_train
    t_numpy = y.to_numpy()
    res = list()
    count = 0
    for i in range(len(X_numpy)):
        pred_price = cp_predictor.PredictByX(X_numpy[i], ALPHA=0.2)
        low = int(round(pred_price['values_range'][0], -2))
        high = int(round(pred_price['values_range'][1], -2))
        y_pred = pred_price['values'][0]
        error = abs((y_pred - t_numpy[i]) / t_numpy[i])
        cp_err = (high - ((high + low) / 2)) / ((high + low) / 2)
        if cp_err <= 0.15:
            print(f"find in {i}, cp_err: {cp_err}")
            res.append(i)
            count += 1
        if count == 10:
            break

    exampleDF_NoPrice = X.iloc[res]
    print(exampleDF_NoPrice)
    exampleDF_NoPrice.to_csv(file_name_no_price, index=False)
    exampleDF = pd.concat([exampleDF_NoPrice, y.iloc[res]], axis=1)
    print(exampleDF)
    exampleDF.to_csv(file_name, index=False)



genExample(full=True)
genExample(full=False)
