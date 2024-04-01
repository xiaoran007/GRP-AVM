"""
Copyright (c) 2024 Tangtangfang Fang

All rights reserved.

This file is part of AVM-GRP.

AVM-GRP is distributed under the GPLv3 License.
See the LICENSE file at the top level of the distribution for details.
"""

from mapie.regression import MapieRegressor
from Datasets.Data import Default, Default_Easy
import os


class CPBuilder(object):
    def __init__(self, pre_fit_model):
        self.PRE_FIT_MODEL = pre_fit_model

    def Make(self, full=True):
        if full:
            X_train, y_train, X_test, y_test = Default(os.path.dirname(__file__))
        else:
            X_train, y_train, X_test, y_test = Default_Easy(os.path.dirname(__file__))
        mapie_reg = MapieRegressor(estimator=self.PRE_FIT_MODEL, n_jobs=-1, verbose=0, cv='prefit')
        print('Start Fit CP')
        mapie_reg.fit(X_test, y_test)
        print('Start Evaluate CP')
        mapie_pred, mapie_pis = mapie_reg.predict(X_test, alpha=0.2)
        print(mapie_pis)
        print(mapie_pred)
        return mapie_reg

