import joblib

from model.src import RF
import os
import pandas as pd


class Predictor(object):
    """
    This class is used for predicting price of houses.
    """

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
        Used by PredictByX().
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

    def PredictByX(self, X):
        """
        Predict the price using the given X, calling the method will change the object's default X value.
        :param X: numpy array, 19 columns if lofi is False, 7 columns if lofi is True
        """
        self.X = X
        return self.Predict()

    @staticmethod
    def numpy2df(numpy_arr, full):
        """
        Convert a numpy array to a pandas dataframe.
        :param numpy_arr: numpy array, 19 columns or 7 columns.
        :param full: Bool, set True if full model is needed
        :return: pandas dataframe with columns name.
        """
        if len(numpy_arr) == 7 and full is False:
            feature_name = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'building_age', 'lat', 'long']
            df = pd.DataFrame([numpy_arr])
            df.columns = feature_name
        else:
            if len(numpy_arr) != 19:
                raise ValueError('X should be 19 columns if lofi is False, 7 columns if lofi is True.')
            feature_name = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view',
                            'condition',
                            'grade',
                            'sqft_above', 'sqft_basement', 'building_age', 'renovated_year', 'lat', 'long',
                            'sqft_living15',
                            'sqft_lot15', 'year', 'month']
            df = pd.DataFrame([numpy_arr])
            df.columns = feature_name
            if full is False:
                df = df[['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'building_age', 'lat', 'long']]
                print(df)
        return df

    def LoadModel(self):
        """
        Load the model, use self.model_sel to select the model type.
        :return: model object
        """
        if self.model_sel == 'RF':
            return RF.RFModel((not self.FULL), self.LANG).Load()

    def CheckModel(self):
        """
        Check if the model is loaded.
        :return: Bool, True if model already loaded
        """
        if self.MODEL is None:
            return False
        else:
            return True


class CpPredictor(Predictor):
    """
    Child class of Predictor, used for predicting range price of properties.
    """
    def __init__(self, X, model_sel="RF", full=True, cwd='./', alpha=0.2):
        """
        :param X: numpy array, 19 or 7 columns.
        :param model_sel: string, model type, ['RF', 'XGB', 'LGBM'], default is 'RF'.
        :param full: Bool, set True if full model is needed.
        :param cwd: string, caller file path, use os.path.dirname(__file__)
        :param alpha: float, alpha value used by CP, default is 0.2.
        """
        super().__init__(X, model_sel, full)
        self.ALPHA = alpha
        self.CWD = cwd
        os.chdir(os.path.dirname(__file__))
        print(f"set dir: {os.getcwd()}")
        self.MODEL = self.LoadModel()
        print(f'load model type: {type(self.MODEL)}')
        os.chdir(self.CWD)
        print(f"set dir back: {self.CWD}")

    def Predict(self):
        """
        only one predict one time. used by PredictByX().
        :return: dict, key 'status' 0 if success, key 'values' contents return values, key 'values_range' return values range
        """
        if self.CheckModel():
            try:
                return_dict = dict()
                print(type(self.MODEL))
                predicted_values, mapie_pis = self.MODEL.predict(self.numpy2df(self.X, self.FULL), alpha=self.ALPHA)
                return_dict['status'] = 0
                return_dict['values'] = predicted_values.tolist()
                values_range = [mapie_pis[0][0][0], mapie_pis[0][1][0]]
                return_dict['values_range'] = values_range
                return_dict['model_type'] = self.model_sel
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

    def PredictByX(self, X, ALPHA=0.2):
        """
        Predict the range price using the given X, calling the method will change the object's default X value and ALPHA value.'
        :param X: numpy array, 19 columns if lofi is False, 7 columns if lofi is True
        :param ALPHA: float, default 0.2, 1 - confidence level
        :return: dict, key 'status' 0 if success, key 'values' contents return
        """
        self.X = X
        self.ALPHA = ALPHA
        return self.Predict()

    def LoadModel(self):
        """
        :return: CP model object
        """
        if self.model_sel == 'RF':
            if self.FULL:
                return joblib.load('object/rev311/RF_CP_Full.mdo')
            else:
                return joblib.load('object/rev311/RF_CP_Easy.mdo')
        elif self.model_sel == 'XGB':
            if self.FULL:
                return joblib.load('object/rev311/XGB_CP_Full.mdo')
            else:
                return joblib.load('object/rev311/XGB_CP_Easy.mdo')
        elif self.model_sel == 'LGBM':
            if self.FULL:
                return joblib.load('object/rev311/LGBM_CP_Full.mdo')
            else:
                return joblib.load('object/rev311/LGBM_CP_Easy.mdo')
        else:
            if self.FULL:
                return joblib.load('object/rev311/RF_CP_Full.mdo')
            else:
                return joblib.load('object/rev311/RF_CP_Easy.mdo')


