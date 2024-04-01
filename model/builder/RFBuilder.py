"""
Copyright (c) 2024 Tangtangfang Fang

All rights reserved.

This file is part of AVM-GRP.

AVM-GRP is distributed under the GPLv3 License.
See the LICENSE file at the top level of the distribution for details.
"""

from sklearn.ensemble import RandomForestRegressor
from Datasets.Data import Default, Default_Easy
import os
from Evaluator import Evaluator


class RFBuilder(object):

    @staticmethod
    def Make(method):
        if method:
            print('Make Full')
            X_train, y_train, X_test, y_test = Default(os.path.dirname(__file__))
        else:
            print('Make Easy')
            X_train, y_train, X_test, y_test = Default_Easy(os.path.dirname(__file__))
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

