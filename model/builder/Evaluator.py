import os
import pandas as pd
import numpy as np

from sklearn.metrics import r2_score, mean_squared_error
from Datasets.Data import Default, Default_Easy


class Evaluator:
    def __init__(self, y_true, y_pred):
        self.y_true = y_true
        self.y_pred = y_pred

    def Evaluate(self, error=0.1):
        """

        Args:
            error: Acceptable error percentage, default: 0.1 means 10%

        Returns:
            [count: int, total: int, acc: double, r2: double, rmse: double]

        """
        count = 0
        total = len(self.y_pred)
        for i in range(total):
            if abs(self.y_pred[i] - self.y_true[i]) < (self.y_true[i] * error):
                count = count + 1

        return count, total, count / total, r2_score(self.y_true, self.y_pred), mean_squared_error(self.y_true, self.y_pred, squared=False)


class ModelEvaluator:
    def __init__(self, preTrainedModel, full):
        self.PreTrainedModel = preTrainedModel
        self.Full = full
        self.Data = self.loadTestSet(full=self.Full)

    @staticmethod
    def loadTestSet(full):
        if full:
            _, _, X_test, y_test = Default(os.path.dirname(__file__))
        else:
            _, _, X_test, y_test = Default_Easy(os.path.dirname(__file__))
        test_df = pd.concat([X_test, y_test], axis=1)
        test_df = test_df.sort_values(by=['price'], ignore_index=True)
        num_rows = len(test_df)
        rows_per_sub_df = num_rows // 10
        remaining_rows = num_rows % 10
        sub_dataframes = list()
        start_index = 0
        for i in range(10):
            end_index = start_index + rows_per_sub_df
            if i < remaining_rows:
                end_index += 1
            sub_df = test_df.iloc[start_index:end_index]
            sub_dataframes.append(sub_df)
            start_index = end_index

        return sub_dataframes


# ModelEvaluator.loadTestSet(True)





