import random

from NLGen.Descriptor import Descriptor
from Datasets.Data import Default, Default_Easy
from model.Predictor import Predictor
import os


def TEST(sel_index, full):
    if full is True:
        X_train, y_train, X_test, y_test = Default(os.path.dirname(__file__))
    else:
        X_train, y_train, X_test, y_test = Default_Easy(os.path.dirname(__file__))
    X_train_numpy = X_train.to_numpy()
    sel = X_train_numpy[sel_index]
    predictor = Predictor(sel,  model_sel='RF', full=full, lang=False, cwd=os.path.dirname(__file__))
    pred_price = predictor.Predict()
    print(pred_price)
    descriptor = Descriptor(sel, pred_price['values'][0], full=full, cwd=os.path.dirname(__file__))
    text = descriptor.GetDescription()
    print(text)
    return pred_price, text


p = list()
text_dict = list()
for i in range(10):
    pred_price, text = TEST(sel_index=random.randint(1, 1000), full=False)
    p.append(pred_price['values'][0])
    text_dict.append(text)

print("-----------------")
for i in range(len(p)):
    print(f"price: {p[i]}, text: {text_dict[i]}")
