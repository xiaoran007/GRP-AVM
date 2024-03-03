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
    true_price = y_train.to_numpy()[sel_index]
    sel = X_train_numpy[sel_index]
    predictor = Predictor(sel,  model_sel='RF', full=full, lang=False, cwd=os.path.dirname(__file__))
    pred_price = predictor.Predict()
    print(pred_price)
    descriptor = Descriptor(sel, pred_price['values'][0], full=full, cwd=os.path.dirname(__file__))
    text = descriptor.generateDescription()
    print(text)
    return pred_price, text, true_price


p = list()
text_dict = list()
true_price_list = list()
for i in range(10):
    pred_price, text, true_price = TEST(sel_index=random.randint(1, 1000), full=True)
    p.append(pred_price['values'][0])
    text_dict.append(text)
    true_price_list.append(true_price)

print("-----------------")
for i in range(len(p)):
    print(f"price: {p[i]}, true_price: {true_price_list[i]}, text: {text_dict[i]}")
