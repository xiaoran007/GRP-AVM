import random

import joblib
from Datasets.Data import Default, Default_Easy
import os
import pandas as pd
from Evaluator import Evaluator


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

def test(train=False):
    if train:
        X_test, y_test, _, _ = Default(os.path.dirname(__file__))
        target = "train"
    else:
        _, _, X_test, y_test = Default(os.path.dirname(__file__))
        target = "test"
    xgb = joblib.load('./XGB_Full.mdo')
    rf = joblib.load('./RF_Full.mdo')
    # rf = joblib.load('../object/RF_Full.mdo')
    lgbm = joblib.load('./LGBM_Full.mdo')
    X_test_numpy = X_test.to_numpy()
    y_test_numpy = y_test.to_numpy()
    for i in range(10):
        # sel = random.randint(0, X_test_numpy.shape[0] - 1)
        sel = i
        pred_xgb = xgb.predict(numpy2df(X_test_numpy[sel], True))
        pred_rf = rf.predict(numpy2df(X_test_numpy[sel], True))
        pred_lgbm = lgbm.predict(numpy2df(X_test_numpy[sel], True))
        true = y_test_numpy[sel]
        err_xgb = abs(round(abs(pred_xgb[0] - true), 2))
        err_rf = abs(round(abs(pred_rf[0] - true), 2))
        err_lgbm = abs(round(abs(pred_lgbm[0] - true), 2))
        print(f"XGB: {pred_xgb[0]}, RF: {pred_rf[0]}, LGBM: {pred_lgbm[0]}, True: {true}")
        print(f"XGB-ERR: {err_xgb}, RF-ERR: {err_rf}, LGBM-ERR: {err_lgbm}")
        print("-----")


def test2(train=False):
    if train:
        X_test, y_test, _, _ = Default(os.path.dirname(__file__))
        target = "train"
    else:
        _, _, X_test, y_test = Default(os.path.dirname(__file__))
        target = "test"
    xgb = joblib.load('./XGB_Full.mdo')
    rf = joblib.load('./RF_Full.mdo')
    # rf = joblib.load('../object/RF_Full.mdo')
    lgbm = joblib.load('./LGBM_Full.mdo')
    pred_xgb = xgb.predict(X_test)
    pred_rf = rf.predict(X_test)
    pred_lgbm = lgbm.predict(X_test)
    print('Start Evaluate')
    count, total, acc, r2, rmse = Evaluator(y_pred=pred_xgb, y_true=y_test.to_numpy()).Evaluate(error=0.2)
    print(f'XGB {target}: count:{count}, total:{total}, acc:{acc}, r2:{r2}, rmse:{rmse}')
    count, total, acc, r2, rmse = Evaluator(y_pred=pred_rf, y_true=y_test.to_numpy()).Evaluate(error=0.2)
    print(f'RF {target}: count:{count}, total:{total}, acc:{acc}, r2:{r2}, rmse:{rmse}')
    count, total, acc, r2, rmse = Evaluator(y_pred=pred_lgbm, y_true=y_test.to_numpy()).Evaluate(error=0.2)
    print(f'LGBM {target}: count:{count}, total:{total}, acc:{acc}, r2:{r2}, rmse:{rmse}')

test2(train=False)
