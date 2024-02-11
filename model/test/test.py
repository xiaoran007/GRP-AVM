import pandas as pd
from model import Predictor


df = pd.read_csv("./data/X_Full_test.csv")
print(df.columns.tolist())
predictor = Predictor.Predictor(X=df, model_sel='RF', lofi=False, lang=False)
print(predictor.Predict())
