import os

from Datasets.Data import DataLoader, Preprocessing, Default, Default_Easy
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
import joblib
import warnings
import pandas as pd
import numpy as np

# Ignore only DeprecationWarning
warnings.filterwarnings("ignore", category=FutureWarning)


def classGenerator(method, normal, random_state, k, full=True):
    if full is True:
        X_train, y_train, X_test, y_test = Default(os.path.dirname(__file__))
        flag = "Full"
    else:
        X_train, y_train, X_test, y_test = Default_Easy(os.path.dirname(__file__))
        flag = "Easy"
    kmeans = KMeans(n_clusters=k, random_state=random_state, n_init='auto')
    kmeans.fit(X_train)
    print(kmeans.labels_)
    try:
        joblib.dump(kmeans, f'./kmeans_model_{flag}.mdo')
        print("Save kmeans object file.")
    except Exception as e:
        print("Error: ", e)

    X_train_numpy = X_train.to_numpy()
    y_train_numpy = y_train.to_numpy()
    class0 = list()
    class1 = list()
    class2 = list()
    class3 = list()
    price0 = list()
    price1 = list()
    price2 = list()
    price3 = list()
    for i in range(len(kmeans.labels_)):
        if kmeans.labels_[i] == 0:
            class0.append(X_train_numpy[i])
            price0.append(y_train_numpy[i])
        elif kmeans.labels_[i] == 1:
            class1.append(X_train_numpy[i])
            price1.append(y_train_numpy[i])
        elif kmeans.labels_[i] == 2:
            class2.append(X_train_numpy[i])
            price2.append(y_train_numpy[i])
        elif kmeans.labels_[i] == 3:
            class3.append(X_train_numpy[i])
            price3.append(y_train_numpy[i])
    print(f"Class 0: {len(class0)}, Class 1: {len(class1)}, Class 2: {len(class2)}, Class 3: {len(class3)}")
    class0_df = pd.DataFrame(class0)
    class1_df = pd.DataFrame(class1)
    class2_df = pd.DataFrame(class2)
    class3_df = pd.DataFrame(class3)
    avg_dict = dict()
    avg_dict[0] = [[round(x, 3) for x in class0_df.mean(axis="rows").tolist()], round(np.mean(price0), 3)]
    avg_dict[1] = [[round(x, 3) for x in class1_df.mean(axis="rows").tolist()], round(np.mean(price1), 3)]
    avg_dict[2] = [[round(x, 3) for x in class2_df.mean(axis="rows").tolist()], round(np.mean(price2), 3)]
    avg_dict[3] = [[round(x, 3) for x in class3_df.mean(axis="rows").tolist()], round(np.mean(price3), 3)]
    try:
        print(avg_dict)
        joblib.dump(avg_dict, f'./class_avg_{flag}.mdo')
        print("Save avg object file.")
    except Exception as e:
        print("Error: ", e)


def Test(method, normal, random_state, k):
    X_train, y_train, X_test, y_test = Default(os.path.dirname(__file__))
    kmeans = KMeans(n_clusters=k, random_state=random_state, n_init='auto')
    # kmeans = AgglomerativeClustering(n_clusters=k)  # k = 4
    kmeans.fit(X_train)
    print(kmeans.labels_)
    KmeansEvaluator(X=X_train, Labels=kmeans.labels_, k=k)


def KmeansEvaluator(X, Labels, k):
    silhouetteScore = silhouette_score(X=X, labels=Labels, metric='euclidean')
    daviesBouldinScore = davies_bouldin_score(X=X, labels=Labels)  # Lower is better
    calinskiHarabaszScore = calinski_harabasz_score(X=X, labels=Labels)  # Higher is better
    print(f'K: {k}, Silhouette Score: {silhouetteScore:.3f}, Davies Bouldin Score: '
          f'{daviesBouldinScore:.3f}, Calinski Harabasz Score: {calinskiHarabaszScore:.3f}')


def getAVG(full=True):
    if full is True:
        X_train, y_train, _, _ = Default(os.path.dirname(__file__))
        flag = "Full"
        feature_name = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
            'sqft_above', 'sqft_basement', 'building_age', 'renovated_year', 'lat', 'long', 'sqft_living15',
            'sqft_lot15', 'year', 'month']
        kmeans = joblib.load('./kmeans_model_Full.mdo')
    else:
        X_train, y_train, _, _ = Default_Easy(os.path.dirname(__file__))
        flag = "Easy"
        feature_name = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'building_age', 'lat', 'long']
        kmeans = joblib.load('./kmeans_model_Easy.mdo')
    X_train_numpy = X_train.to_numpy()
    y_train_numpy = y_train.to_numpy()
    class0 = pd.DataFrame()
    class1 = pd.DataFrame()
    class2 = pd.DataFrame()
    class3 = pd.DataFrame()
    for i in X_train_numpy:
        df = numpy2df(i, full=full)
        train = kmeans.predict(df)
        print(train)


def numpy2df(numpy_arr, full):
    if full is True:
        feature_name = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view', 'condition',
                        'grade',
                        'sqft_above', 'sqft_basement', 'building_age', 'renovated_year', 'lat', 'long', 'sqft_living15',
                        'sqft_lot15', 'year', 'month']
    else:
        feature_name = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'building_age', 'lat', 'long']
    df = pd.DataFrame([numpy_arr])
    df.columns = feature_name
    return df


# getAVG()

# for i in range(2, 11):
#     Test(method="keep", normal="MinMax", random_state=62, k=i)

classGenerator(method="keep", normal="MinMax", random_state=62, k=4, full=True)
classGenerator(method="keep", normal="MinMax", random_state=62, k=4, full=False)
