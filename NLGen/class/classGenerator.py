import os

from Datasets.Data import DataLoader, Preprocessing, Default, Default_Easy
from sklearn.cluster import KMeans
import seaborn as sns
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
import joblib
import warnings

# Ignore only DeprecationWarning
warnings.filterwarnings("ignore", category=FutureWarning)


def classGenerator(method, normal, random_state, k, full=True):
    if full is True:
        X_train, y_train, X_test, y_test = Default(os.path.dirname(__file__))
        flag = "Full"
    else:
        X_train, y_train, X_test, y_test = Default_Easy(os.path.dirname(__file__))
        flag = "Easy"
    print(X_train)
    kmeans = KMeans(n_clusters=k, random_state=random_state, n_init='auto')
    kmeans.fit(X_train)
    print(kmeans.labels_)
    try:
        joblib.dump(kmeans, f'./kmeans_model_{flag}.mdo')
    except Exception as e:
        print("Error: ", e)


def Test(method, normal, random_state, k):
    X_train, y_train, X_test, y_test = Default(os.path.dirname(__file__))
    kmeans = KMeans(n_clusters=k, random_state=random_state, n_init='auto')
    # kmeans = AgglomerativeClustering(n_clusters=k)  # k = 4
    kmeans.fit(X_train)
    print(kmeans.labels_)
    sns.boxplot(x=kmeans.labels_, y=y_train)
    # plt.show()
    KmeansEvaluator(X=X_train, Labels=kmeans.labels_, k=k)


def KmeansEvaluator(X, Labels, k):
    silhouetteScore = silhouette_score(X=X, labels=Labels, metric='euclidean')
    daviesBouldinScore = davies_bouldin_score(X=X, labels=Labels)  # Lower is better
    calinskiHarabaszScore = calinski_harabasz_score(X=X, labels=Labels)  # Higher is better
    print(f'K: {k}, Silhouette Score: {silhouetteScore:.3f}, Davies Bouldin Score: '
          f'{daviesBouldinScore:.3f}, Calinski Harabasz Score: {calinskiHarabaszScore:.3f}')


# for i in range(2, 11):
#     Test(method="keep", normal="MinMax", random_state=62, k=i)

classGenerator(method="keep", normal="MinMax", random_state=62, k=4, full=False)
