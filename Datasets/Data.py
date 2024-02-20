import os
import sys
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, Normalizer, PowerTransformer


class DataLoader(object):
    def __init__(self, dataset_name=None):
        self.DatasetName = dataset_name

    def GetData(self):
        if self.DatasetName is None:
            url = 'kc_house_data.csv'
            return self.dataset_loader(url=url)
        else:
            pass

    def GetDataKeepDate(self):
        if self.DatasetName is None:
            url = 'kc_house_data.csv'
            return self.dataset_loader_KeepDate(url=url)
        else:
            pass

    @staticmethod
    def dataset_loader(url):
        df = pd.read_csv(url, delimiter=',')
        X = df.drop(['id', 'date', 'price'], axis=1)
        y = df['price']
        X = MinMaxScaler().fit_transform(X)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0, stratify=None)
        X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.125, random_state=0,
                                                          stratify=None)

        print(X_train.shape)

        return X_train, y_train, X_val, y_val, X_test, y_test

    @staticmethod
    def dataset_loader_KeepDate(url):
        df = pd.read_csv(url, delimiter=',')
        df['date'] = pd.to_datetime(df['date'])
        df['year'] = df['date'].apply(lambda date: date.year)
        df['month'] = df['date'].apply(lambda date: date.month)
        df = df.drop('date', axis=1)
        X = df.drop(['id', 'price'], axis=1)
        y = df['price']
        X = MinMaxScaler().fit_transform(X)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0, stratify=None)
        X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.125, random_state=0,
                                                          stratify=None)

        print(X_train.shape)

        return X_train, y_train, X_val, y_val, X_test, y_test

    @staticmethod
    def Load(flag=False, method="keep", normal="MinMax", full=True, lofi=False, high=2e6, low=0):
        """

        Args:
            if flag is set, ignore other parameters.
            flag: full or lofi load.
            high: remove
            low: remove
            lofi: drop rows?
            full: set False to use subset features. ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'building_age', 'lat', 'long']
            normal: "MinMax", "Normal", "box-cox", "yeo-johnson" or "None"
            method: "keep" will trans "date" to "year" and "month", "drop" will drop "date"

        Returns:
            [X, y]

        """
        url = 'kc_house_data.csv'
        df = pd.read_csv(url, delimiter=',')
        if flag is True:
            if full is True:
                df['date'] = pd.to_datetime(df['date'])
                df['year'] = df['date'].apply(lambda date: date.year)
                df['month'] = df['date'].apply(lambda date: date.month)
                df['building_age'] = df['year'] - df['yr_built']
                df['renovated_year'] = DataLoader.Trans(year_renovated=df['yr_renovated'].tolist(), year=df['year'].tolist(), building_age=df['building_age'].tolist())
                X = df[['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view', 'condition',
                        'grade',
                        'sqft_above', 'sqft_basement', 'building_age', 'renovated_year', 'lat', 'long', 'sqft_living15',
                        'sqft_lot15', 'year', 'month']]
                y = df['price']
                return X, y
            else:
                df['date'] = pd.to_datetime(df['date'])
                df['year'] = df['date'].apply(lambda date: date.year)
                df['month'] = df['date'].apply(lambda date: date.month)
                df['building_age'] = df['year'] - df['yr_built']
                df['renovated_year'] = DataLoader.Trans(year_renovated=df['yr_renovated'].tolist(), year=df['year'].tolist(), building_age=df['building_age'].tolist())
                X = df[['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'building_age', 'lat', 'long']]
                y = df['price']
                return X, y
        # if flag is unset:
        if lofi:
            df = df.drop(df[df.price >= high].index)
            df = df.drop(df[df.price <= low].index)
        if method == "keep":
            df['date'] = pd.to_datetime(df['date'])
            df['year'] = df['date'].apply(lambda date: date.year)
            df['month'] = df['date'].apply(lambda date: date.month)
            df = df.drop('date', axis=1)
            X = df.drop(['id', 'price'], axis=1)
        elif method == "drop":
            X = df.drop(['id', 'date', 'price'], axis=1)
        else:
            X = df.drop(['id', 'date', 'price'], axis=1)
        y = df['price']
        if normal == "MinMax":
            print("normal is MinMax")
            X = MinMaxScaler().fit_transform(X)
        elif normal == "Normal":
            X = Normalizer().fit_transform(X)
        elif normal == "None":
            print("normal is None")
            pass
        return X, y

    @staticmethod
    def Trans(year_renovated, year, building_age):
        return_list = list()
        for i in range(len(year_renovated)):
            if year_renovated[i] == 0:
                return_list.append(building_age[i])
            else:
                return_list.append(year[i] - year_renovated[i])
        return return_list


class Preprocessing(object):
    def __init__(self, X, y, random_state=42):

        self.X = X
        self.y = y
        self.RandomState = random_state

    def DoNothing(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=self.RandomState, stratify=None)
        return X_train, y_train, X_test, y_test

    def LogTransform(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=self.RandomState, stratify=None)
        X_train_log = np.log1p(X_train)
        X_test_log = np.log1p(X_test)
        y_train_log = np.log1p(y_train)
        y_test_log = np.log1p(y_test)
        return X_train, y_train, X_test, y_test, X_train_log, y_train_log, X_test_log, y_test_log


def Default(cwd):
    """

    :param cwd: current work path
    :return: pandas DataFrame
    """
    os.chdir(os.path.dirname(__file__))
    print(f"set dir: {os.getcwd()}")
    X, y = DataLoader().Load(flag=True, full=True)
    X_train, y_train, X_test, y_test = Preprocessing(X, y, random_state=62).DoNothing()
    os.chdir(cwd)
    print(f"set dir back: {cwd}")
    return X_train, y_train, X_test, y_test


def Default_Easy(cwd):
    """

        :param cwd: current work path
        :return: pandas DataFrame
    """
    os.chdir(os.path.dirname(__file__))
    print(f"set dir: {os.getcwd()}")
    X, y = DataLoader().Load(flag=True, full=False)
    X_train, y_train, X_test, y_test = Preprocessing(X, y, random_state=62).DoNothing()
    os.chdir(cwd)
    print(f"set dir back: {cwd}")
    return X_train, y_train, X_test, y_test
