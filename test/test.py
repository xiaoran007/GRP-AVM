"""
Copyright (c) 2024 Tangtangfang Fang

All rights reserved.

This file is part of AVM-GRP.

AVM-GRP is distributed under the GPLv3 License.
See the LICENSE file at the top level of the distribution for details.
"""

import random

from NLGen.Descriptor import Descriptor
from Datasets.Data import Default, Default_Easy
from model.Predictor import Predictor, CpPredictor
import os


def TEST(sel_index, full):
    if full is True:
        X_train, y_train, X_test, y_test = Default(os.path.dirname(__file__))
    else:
        X_train, y_train, X_test, y_test = Default_Easy(os.path.dirname(__file__))
    X_train_numpy = X_train.to_numpy()
    true_price = y_train.to_numpy()[sel_index]
    sel = X_train_numpy[sel_index]
    predictor = Predictor(sel,  model_sel='RF', full=full, lang=False, cwd=os.path.dirname(__file__))
    pred_price = predictor.Predict()
    print(pred_price)
    descriptor = Descriptor(sel, pred_price['values'][0], full=full, cwd=os.path.dirname(__file__))
    text = descriptor.generateDescription()
    print(text)
    return pred_price, text, true_price





def FULL_TEST():
    predictor = CpPredictor(X=None, full=True, alpha=None, cwd=os.path.dirname(__file__))
    descriptor = Descriptor(X=None, predicted_price=None, full=True, cwd=os.path.dirname(__file__))
    X_train, y_train, X_test, y_test = Default(os.path.dirname(__file__))
    X_test_numpy = X_test.to_numpy()
    true_prices = y_test.to_numpy()
    p = list()
    text_dict = list()
    true_price_list = list()
    for i in range(10):
        sel_index = random.randint(0, len(X_test_numpy))
        pred_price = predictor.PredictByX(X=X_test_numpy[sel_index], ALPHA=0.2)
        text = descriptor.GenerateDescription(X=X_test_numpy[sel_index], predicted_price=pred_price['values'][0], full=True)
        true_price = true_prices[sel_index]
        p.append(pred_price['values'][0])
        text_dict.append(text)
        true_price_list.append(true_price)

    print("-----------------")
    for i in range(len(p)):
        print(f"price: {p[i]}, true_price: {true_price_list[i]}, text: {text_dict[i]}")


FULL_TEST()
