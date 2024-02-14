from sklearn.metrics import r2_score, mean_squared_error


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





