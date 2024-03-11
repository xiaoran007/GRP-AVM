from mapie.regression import MapieRegressor
from sklearn.ensemble import RandomForestRegressor
import joblib
from Datasets.Data import Default, Default_Easy
import os
from model.Predictor import Predictor
import pandas as pd
from Evaluator import Evaluator


def Make(method):
    if method == 'Full':
        print('Make Full')
        X_train, y_train, X_test, y_test = Default(os.path.dirname(__file__))
    elif method == 'Easy':
        print('Make Easy')
        X_train, y_train, X_test, y_test = Default_Easy(os.path.dirname(__file__))
    else:
        X_train, y_train, X_test, y_test = Default(os.path.dirname(__file__))
    rf = RandomForestRegressor(n_jobs=-1, criterion='squared_error', verbose=0)
    rf.fit(X=X_train, y=y_train)
    y_pred_train = rf.predict(X=X_train)
    y_pred_test = rf.predict(X=X_test)
    print('Start Evaluate')
    count, total, acc, r2, rmse = Evaluator(y_pred=y_pred_train, y_true=y_train.to_numpy()).Evaluate(error=0.2)
    print(f'Train: count:{count}, total:{total}, acc:{acc}, r2:{r2}, rmse:{rmse}')
    count, total, acc, r2, rmse = Evaluator(y_pred=y_pred_test, y_true=y_test.to_numpy()).Evaluate(error=0.2)
    print(f'Test: count:{count}, total:{total}, acc:{acc}, r2:{r2}, rmse:{rmse}')

    # joblib.dump(rf, f'RF_{method}.mdo')
    print('Save model')
    return rf


if __name__ == '__main__':
    Make(method='Easy')
    Make(method='Full')
