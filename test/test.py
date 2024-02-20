from NLGen.Descriptor import Descriptor
from Datasets.Data import Default, Default_Easy
from model.Predictor import Predictor
import os


def TEST():
    X_train, y_train, X_test, y_test = Default(os.path.dirname(__file__))
    X_train_numpy = X_train.to_numpy()
    sel = X_train_numpy[0]
    predictor = Predictor(sel,  model_sel='RF', full=True, lang=False, cwd=os.path.dirname(__file__))
    pred_price = predictor.Predict()
    print(pred_price)
    descriptor = Descriptor(sel, pred_price['values'][0], full=True, cwd=os.path.dirname(__file__))
    text = descriptor.GetDescription()
    print(text)


TEST()
