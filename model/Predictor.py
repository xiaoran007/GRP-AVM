import joblib

from model.src import RF
import os
import pandas as pd


class Predictor(object):

    def __init__(self, X, model_sel="RF", full=True, lang=False, cwd='./'):
        """
        :param X: numpy array, 19 columns if lofi is False, 7 columns if lofi is True
        :param model_sel: string, model type, support 'RF'
        :param full: Bool, set False if easy model is needed
        :param lang: Bool, set True if descriptions is needed
        """
        self.X = X
        self.model_sel = model_sel
        self.FULL = full
        self.LANG = lang
        os.chdir(os.path.dirname(__file__))
        print(f"set dir: {os.getcwd()}")
        self.MODEL = self.LoadModel()
        os.chdir(cwd)
        print(f"set dir back: {cwd}")

    def Predict(self):
        """
        :return: dict, key 'status' 0 if success, key 'values' contents return values
        """
        if self.CheckModel():
            try:
                return_dict = dict()
                predicted_values = self.MODEL.predict(self.numpy2df(self.X, self.FULL))
                return_dict['status'] = 0
                return_dict['values'] = predicted_values.tolist()
                return return_dict
            except Exception as e:
                print('Error: ', e)
                return_dict = dict()
                return_dict['status'] = -1
                return_dict['values'] = 'Error when predict.'
                return return_dict
        else:
            return_dict = dict()
            return_dict['status'] = -2
            return_dict['values'] = 'Model unload.'
            return return_dict

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

    def LoadModel(self):
        """
        :return: model object
        """
        if self.model_sel == 'RF':
            return RF.RFModel((not self.FULL), self.LANG).Load()

    def CheckModel(self):
        """
        :return: Bool, True if model already loaded
        """
        if self.MODEL is None:
            return False
        else:
            return True


class CpPredictor(Predictor):
    def __init__(self, X, model_sel="RF", full=True, cwd='./'):
        super(CpPredictor, self).__init__(X, model_sel, full)
        os.chdir(os.path.dirname(__file__))
        print(f"set dir: {os.getcwd()}")
        self.MODEL = self.LoadModel()
        os.chdir(cwd)
        print(f"set dir back: {cwd}")

    def Predict(self):
        """
        :return: dict, key 'status' 0 if success, key 'values' contents return values, key 'values_range' return values range
        """
        if self.CheckModel():
            try:
                return_dict = dict()
                predicted_values, mapie_pis = self.MODEL.predict(self.numpy2df(self.X, self.FULL))
                return_dict['status'] = 0
                return_dict['values'] = predicted_values.tolist()
                values_range = [mapie_pis[0][0][0], mapie_pis[0][1][0]]
                return_dict['values_range'] = values_range
                return return_dict
            except Exception as e:
                print('Error: ', e)
                return_dict = dict()
                return_dict['status'] = -1
                return_dict['values'] = 'Error when predict.'
                return return_dict
        else:
            return_dict = dict()
            return_dict['status'] = -2
            return_dict['values'] = 'Model unload.'
            return return_dict

    def LoadModel(self):
        """
        :return: model object
        """
        if self.FULL is True:
            return joblib.load('object/MAPIE_Full.mdo')
        else:
            return joblib.load('object/MAPIE_Easy.mdo')


