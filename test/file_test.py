"""
Copyright (c) 2024 Tangtangfang Fang

All rights reserved.

This file is part of AVM-GRP.

AVM-GRP is distributed under the GPLv3 License.
See the LICENSE file at the top level of the distribution for details.
"""

from Datasets.Data import Default, Default_Easy
import pandas as pd
import os

def genExample(full=True):
    if full:
        X_train, y_train, X_test, y_test = Default(os.path.dirname(__file__))
        file_name = 'resources/Full_example.csv'
    else:
        X_train, y_train, X_test, y_test = Default_Easy(os.path.dirname(__file__))
        file_name = 'resources/Easy_example.csv'
    exampleDF = X_test.head(10)
    print(exampleDF)
    exampleDF.to_csv(file_name, index=False)


genExample(full=True)
genExample(full=False)
