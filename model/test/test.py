import pandas as pd
import numpy as np
from model import Predictor


df = pd.read_csv("./data/X_Full_test.csv")
print(df.columns.tolist())
predictor = Predictor.Predictor(X=df, model_sel='RF', lofi=False, lang=False)
predicted_dict = predictor.Predict()
if predicted_dict['status'] == 0:
    values = predicted_dict['values']
    y_df = pd.read_csv("./data/y_Full_test.csv")["price"].to_numpy()
    for i in range(len(y_df)):
        print(f'Predicted: {values[i]}, Actual: {y_df[i]}, Err: {np.abs(values[i] - y_df[i]): .1f}, Percent: {(np.abs(values[i] - y_df[i])) / y_df[i] * 100:.1f}')

# print(predictor.Predict())
