from Datasets.Data import Default, Default_Easy
import joblib
import pandas as pd


class Descriptor(object):
    def __init__(self, X, predicted_price, full=True):
        self.X = X
        self.FULL = full
        self.PRICE = predicted_price
        self.KMEANS = None
        self.AVG = None
        self.TRANSFORMERS = None
        self.LoadObject()

    def LoadObject(self):
        try:
            if self.FULL is True:
                self.KMEANS = joblib.load('./class/kmeans_model_Full.mdo')
                self.AVG = joblib.load('./class/class_avg_Full.mdo')
            else:
                self.KMEANS = joblib.load('./class/kmeans_model_Easy.mdo')
                self.AVG = joblib.load('./class/class_avg_Easy.mdo')
        except Exception as e:
            print('Error: ', e)

    def GetDescription(self):
        if self.KMEANS is None or self.AVG is None:
            print("Object file not load.")
            return
        else:
            df = Descriptor.numpy2df(numpy_arr=self.X, full=self.FULL)
            X_class = self.KMEANS.predict(df)[0]
            avg_X_in_class = self.AVG[X_class][0]
            avg_price_in_class = self.AVG[X_class][1]
            if self.FULL is True:
                text = (f"The expected property price is {'higher' if self.PRICE >= avg_price_in_class else 'lower'} than "
                        f"average for this type of property due to the {'high' if Descriptor.compareMeansByFeatureName(avg_X_in_class, self.X, feature_name='grade', full=True) else 'low'} grade, "
                        f"the living size is {'larger' if Descriptor.compareMeansByFeatureName(avg_X_in_class, self.X, feature_name='sqft_living', full=True) else 'smaller'} than average, "
                        f"which means large {'positive' if Descriptor.compareMeansByFeatureName(avg_X_in_class, self.X, feature_name='sqft_living', full=True) else 'negative'} to the price.")
                return text


    @staticmethod
    def numpy2df(numpy_arr, full):
        if full is True:
            feature_name = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view',
                            'condition',
                            'grade',
                            'sqft_above', 'sqft_basement', 'building_age', 'renovated_year', 'lat', 'long',
                            'sqft_living15',
                            'sqft_lot15', 'year', 'month']
        else:
            feature_name = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'building_age', 'lat', 'long']
        df = pd.DataFrame([numpy_arr])
        df.columns = feature_name
        return df

    @staticmethod
    def compareMeansByFeatureName(avg_list, X, feature_name, full=True):
        if full is True:
            name_map = {'bedrooms': 0, 'bathrooms': 1, 'sqft_living': 2, 'sqft_lot': 3, 'floors': 4, 'waterfront': 5,
                        'view': 6,
                        'condition': 7,
                        'grade': 8,
                        'sqft_above': 9, 'sqft_basement': 10, 'building_age': 11, 'renovated_year': 12, 'lat': 13,
                        'long': 14,
                        'sqft_living15': 15,
                        'sqft_lot15': 16, 'year': 17, 'month': 18}
        else:
            name_map = {'bedrooms': 0, 'bathrooms': 1, 'sqft_living': 2, 'sqft_lot': 3, 'building_age': 4, 'lat': 5, 'long': 6}
        if feature_name in name_map.keys():
            return X[name_map[feature_name]] >= avg_list[name_map[feature_name]]
        else:
            return None