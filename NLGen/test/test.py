import joblib
from Datasets.Data import Default
import os

X_train, y_train, X_test, y_test = Default(os.path.dirname(__file__))
kmeans = joblib.load('../class/kmeans_model.mdo')
train = kmeans.predict(X_train)
test = kmeans.predict(X_test)
print(train)
print(len(train))
print(test)
print(len(test))
