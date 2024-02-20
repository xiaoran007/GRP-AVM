from NLGen.Descriptor import Descriptor
from Datasets.Data import Default, Default_Easy
from model.Predictor import Predictor
import os


def TEST():
    X_train, y_train, X_test, y_test = Default(os.path.dirname(__file__))
    X_train_numpy = X_train.to_numpy()
    predictor = Predictor(X_train_numpy[0],  model_sel='RF', full=True, lang=False, cwd=os.path.dirname(__file__))
    pred_price = predictor.Predict()
    print(pred_price)


TEST()
