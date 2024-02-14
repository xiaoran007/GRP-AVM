import os

from Datasets.Data import DataLoader, Preprocessing
from sklearn.cluster import KMeans
import seaborn as sns
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
import joblib
import warnings

# Ignore only DeprecationWarning
warnings.filterwarnings("ignore", category=FutureWarning)


def classGenerator(method, normal, random_state, k):
    X, y = DataLoader().Load(method=method, normal=normal, lofi=False)
    X_train, y_train, X_test, y_test = Preprocessing(X, y, random_state=random_state).DoNothing()
    kmeans = KMeans(n_clusters=k, random_state=random_state, n_init='auto')
    kmeans.fit(X_train)
    print(kmeans.labels_)
    os.chdir(os.path.dirname(__file__))
    joblib.dump(kmeans, './kmeans_model.mdo')


def Test(method, normal, random_state, k):
    X, y = DataLoader().Load(method=method, normal=normal, lofi=False)
    X_train, y_train, X_test, y_test = Preprocessing(X, y, random_state=random_state).DoNothing()
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

classGenerator(method="keep", normal="MinMax", random_state=62, k=4)
