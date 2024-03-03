from Datasets.Data import Default, Default_Easy
import joblib
import pandas as pd
import os


class Descriptor(object):
    def __init__(self, X, predicted_price, full=True, cwd='./'):
        self.X = X
        self.FULL = full
        self.PRICE = predicted_price
        self.IMPORTANCE = self.getFeaturesImportance(self.FULL)
        self.KMEANS = None
        self.AVG = None
        self.TRANSFORMERS = None
        os.chdir(os.path.dirname(__file__))
        print(f"set dir: {os.getcwd()}")
        self.LoadObject()
        os.chdir(cwd)
        print(f"set dir back: {cwd}")

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
                        f"average for this type of property due to the {'higher' if Descriptor.compareMeansByFeatureName(avg_X_in_class, self.X, feature_name='grade', full=True) else 'lower'} grade, "
                        f"the living size is {'larger' if Descriptor.compareMeansByFeatureName(avg_X_in_class, self.X, feature_name='sqft_living', full=True) else 'smaller'} than average, "
                        f"which means {'positive' if Descriptor.compareMeansByFeatureName(avg_X_in_class, self.X, feature_name='sqft_living', full=True) else 'negative'} to the price.")
            else:
                text = (f"The expected property price is {'higher' if self.PRICE >= avg_price_in_class else 'lower'} than "
                        f"average for this type of property due to the {'higher' if Descriptor.compareMeansByFeatureName(avg_X_in_class, self.X, feature_name='sqft_living', full=False) else 'lower'} living areas, "
                        f"the lot size is {'larger' if Descriptor.compareMeansByFeatureName(avg_X_in_class, self.X, feature_name='sqft_lot', full=False) else 'smaller'} than average, "
                        f"which means {'positive' if Descriptor.compareMeansByFeatureName(avg_X_in_class, self.X, feature_name='sqft_lot', full=False) else 'negative'} to the price. "
                        f"Also, building age is {'older' if Descriptor.compareMeansByFeatureName(avg_X_in_class, self.X, feature_name='building_age', full=False) else 'younger'} than average, it "
                        f"{'decreases' if Descriptor.compareMeansByFeatureName(avg_X_in_class, self.X, feature_name='building_age', full=False) else 'increases'} the price.")
            return text

    def generateDescription(self):
        pos_cons_dict = self.generatePosAndCons()
        if pos_cons_dict['status'] is False:
            print("Description not generated.")
            return "Description not generated."
        else:
            description = ""
            if pos_cons_dict['overall'] == 'positive':
                description = description + "The expected property price is higher than average for this type of property due to the"
                if len(pos_cons_dict['positive']) == 1:
                    description = description + f" higher {pos_cons_dict['positive'][0]}"
                elif len(pos_cons_dict['positive']) > 1:
                    description = description + f" higher {pos_cons_dict['positive'][0]} and {pos_cons_dict['positive'][1]}."
                if len(pos_cons_dict['negative']) > 0:
                    description = description + f" However, the lower {pos_cons_dict['negative'][0]} may decrease the price we predicted."
                return description
            else:
                description = description + "The expected property price is lower than average for this type of property."
                if len(pos_cons_dict['positive']) > 0:
                    description = description + f" Although the {pos_cons_dict['positive'][0]} is higher than average,"
                if len(pos_cons_dict['negative']) > 0:
                    description = description + f" the lower {pos_cons_dict['negative'][0]} reduced price to a large extent."
                return description




    def generatePosAndCons(self):
        """

        :return: dict, first check "status" key, if True, then "overall" and "positive" and "negative" keys are returned.
        """
        if self.KMEANS is None or self.AVG is None:
            print("Object file not load.")
            status = False
            return {'status': status, 'overall': '', 'positive': [], 'negative': []}
        else:
            df = Descriptor.numpy2df(numpy_arr=self.X, full=self.FULL)
            X_class = self.KMEANS.predict(df)[0]
            avg_X_in_class = self.AVG[X_class][0]
            avg_price_in_class = self.AVG[X_class][1]
            print(f'pred price: {self.PRICE}, avg price: {avg_price_in_class}')
            if self.PRICE >= avg_price_in_class:
                overall = 'positive'
            else:
                overall = 'negative'
            positive = list()
            negative = list()
            for i in self.IMPORTANCE:
                if Descriptor.compareMeansByFeatureName(avg_X_in_class, self.X, feature_name=i, full=self.FULL):
                    positive.append(i)
                else:
                    negative.append(i)
            status = True
            print(f'pos: {len(positive)}, neg: {len(negative)}')
            return {'status': status, 'overall': overall, 'positive': positive, 'negative': negative}



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
        """

        :param avg_list: mean value of features
        :param X: predicted features
        :param feature_name: feature name
        :param full: set True for full features, False for easy features
        :return: True for positive, False for negative
        """
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

    @staticmethod
    def getFeaturesImportance(full=True):
        if full is True:
            feature_importance_order = ['grade', 'sqft_living', 'lat', 'long', 'sqft_living15', 'building_age', 'waterfront',
                                        'sqft_above', 'bathrooms', 'sqft_lot', 'sqft_lot15', 'view', 'renovated_year',
                                        'sqft_basement', 'month', 'condition', 'bedrooms', 'floors', 'year']
        else:
            feature_importance_order = ['sqft_living', 'lat', 'long', 'sqft_lot', 'building_age', 'bathrooms', 'bedrooms']
        return feature_importance_order
