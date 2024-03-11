import time
from NLGen.Descriptor import Descriptor
from Datasets.Data import Default, Default_Easy
from model.Predictor import Predictor, CpPredictor
import os
import json
import pandas as pd
import json
import joblib

Full_feature_names = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view',
                      'condition',
                      'grade',
                      'sqft_above', 'sqft_basement', 'building_age', 'renovated_year', 'lat', 'long',
                      'sqft_living15',
                      'sqft_lot15', 'year', 'month']

Easy_feature_names = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'building_age', 'lat', 'long']
year = 2014
month = 6


class RecordEventHandler(object):
    """
    This class handles the recording of predictions made by the code assistant.
    """
    def __init__(self):
        """
        Initialize the RecordEventHandler class.
        """
        self.enable = True

    def setEnable(self):
        self.enable = True

    def setDisable(self):
        self.enable = False

    def generateID(self):
        """
        Generate a unique ID for each prediction.
        :return: string, unique ID
        """
        if self.enable:
            current_time = str(int(time.time()))
            rID = current_time[-6:]
        else:
            rID = '******'
        return rID

    def HandleEvent(self, status, price, description, features, model_sel, confidence_level):
        """
        Record a prediction event.
        :param status: list, A list of boolean values indicating the status of the LLM, full model, CP, hidden, and model selection.
        :param price: float, The predicted price.
        :param description: str, The predicted description.
        :param features: list, The input features.
        :param model_sel: str, The model selection. [RF, XGB, LGBM]
        :param confidence_level: float, The confidence level.
        :return: str, The result ID if enable.
        """
        if self.enable:
            rID = self.generateID()
            rec_list = json.load(open('records/rec.json', 'r'))
            joblib.dump({'rID': rID, 'status': status,
                         'features': features, 'price': price, 'text': description, 'model_sel': model_sel, 'confidence_level': confidence_level}, f'./records/{rID}.record')
            rec_list.append(rID)
            json.dump(rec_list, open('records/rec.json', 'w'))
            return f"Result ID is {rID}"
        else:
            return 'This prediction will not be recorded.'

    @staticmethod
    def checkIfRecordExists(rID):
        """
        Check if the record exists.
        :param rID: str, The record ID.
        :return: bool, True if the record exists.
        """
        rec_list = json.load(open('records/rec.json', 'r'))
        if rID in rec_list:
            return True
        else:
            return False

    def SearchRecord(self, rID):
        """
        Search the record.
        :param rID: str, The record ID.
        :return: dict, The record values, if rID not exists, return None.
        """
        if self.checkIfRecordExists(rID):
            record_values = joblib.load(f'./records/{rID}.record')
            return record_values
        else:
            return None


class ProSettingsEventHandler(object):
    """
    handler for pro settings
    """
    def __init__(self, request_dict):
        """
        Initialize the ProSettingsEventHandler class.
        :param request_dict: request form in dict
        """
        self.requestDict = request_dict

    def getControlArgs(self):
        """
        Get the control args.
        :return: list of control args in "enable_llm, enable_full, enable_cp, cp_values, enable_hidden, model_sel"
        """
        if self.requestDict.get('llm') is not None:
            enable_llm = True
        else:
            enable_llm = False
        if self.requestDict.get('full') is not None:
            enable_full = True
        else:
            enable_full = False
        if self.requestDict.get('cp') is not None:
            enable_cp = True
            cp_values = float(self.requestDict.get('cp_value'))
        else:
            enable_cp = False
            cp_values = 0.0
        if self.requestDict.get('hidden') is not None:
            enable_hidden = True
        else:
            enable_hidden = False
        if self.requestDict.get('model') is not None:
            model_sel = self.requestDict.get('model')
        else:
            model_sel = 'RF'
        return enable_llm, enable_full, enable_cp, cp_values, enable_hidden, model_sel


class BackendEventHandler(object):
    """
    This class handles the backend events.
    """
    def __init__(self):
        """
        Initialize the BackendEventHandler class. Preload the object files.
        """
        self.FullRFPredictor = CpPredictor(X=None, model_sel='RF', full=True, alpha=0.2, cwd=os.path.dirname(__file__))
        self.FullXGBPredictor = CpPredictor(X=None, model_sel='XGB', full=True, alpha=0.2, cwd=os.path.dirname(__file__))
        self.FullLGBMPredictor = CpPredictor(X=None, model_sel='LGBM', full=True, alpha=0.2, cwd=os.path.dirname(__file__))
        self.EasyRFPredictor = CpPredictor(X=None, model_sel='RF', full=False, alpha=0.2, cwd=os.path.dirname(__file__))
        self.EasyXGBPredictor = CpPredictor(X=None, model_sel='XGB', full=False, alpha=0.2, cwd=os.path.dirname(__file__))
        self.EasyLGBMPredictor = CpPredictor(X=None, model_sel='LGBM', full=False, alpha=0.2, cwd=os.path.dirname(__file__))
        self.FullDescriptor = Descriptor(X=None, predicted_price=None, full=True, cwd=os.path.dirname(__file__))
        self.EasyDescriptor = Descriptor(X=None, predicted_price=None, full=False, cwd=os.path.dirname(__file__))
        self.RecordSearcher = RecordEventHandler()

    def HandleNormalRequest(self, form_dict, full=True, alpha=0.2):
        """
        Handle the normal request.
        :param form_dict: dict, request form in dict
        :param full: bool, set True to use full model.
        :param alpha: float, The alpha value for the CP predictor.
        :return: features, pred_price, text
        """
        if full:
            features = self.DataTrans(form_dict, data_class='advance')
        else:
            features = self.DataTrans(form_dict, data_class='default')
        x = self.DataPreprocessing(form_dict, full=full)
        pred_price, text = self.handleRequest(x, model_sel='RF', full=full, alpha=alpha)
        return features, pred_price, text

    def HandleProSingleRequest(self, form_dict):
        """
        Handle the pro single request.
        :param form_dict: dict, request form in dict
        :return: features, pred_price, text, rID_str, model_sel, confidence_level
        """
        proSettingsHandler = ProSettingsEventHandler(request_dict=form_dict)
        recordHandler = RecordEventHandler()
        enable_llm, enable_full, enable_cp, cp_values, enable_hidden, model_sel = proSettingsHandler.getControlArgs()
        if enable_hidden:
            recordHandler.setDisable()
        else:
            recordHandler.setEnable()
        if enable_full:
            features = self.DataTrans(form_dict, data_class='advance')
        else:
            features = self.DataTrans(form_dict, data_class='default')
        x = self.DataPreprocessing(form_dict, full=enable_full)
        if enable_cp:
            alpha = 1 - cp_values
        else:
            alpha = 0.2
            cp_values = 0.8
        pred_price, text = self.handleRequest(x, model_sel=model_sel, full=enable_full, alpha=alpha)
        rID_str = recordHandler.HandleEvent(status=[enable_llm, enable_full, enable_cp, cp_values, enable_hidden, model_sel], price=pred_price, description=text, features=features, model_sel=model_sel, confidence_level=cp_values)
        return features, pred_price, text, rID_str, model_sel, cp_values

    def HandleProBatchRequest(self, form_dict, file_path):
        """
        Handle the pro batch request.
        :param form_dict: dict, request form in dict
        :param file_path: str, the file path of the request file
        :return: predicts_length, predict_results, model_sel, confidence_level
        """
        proSettingsHandler = ProSettingsEventHandler(request_dict=form_dict)
        enable_llm, enable_full, enable_cp, cp_values, enable_hidden, model_sel = proSettingsHandler.getControlArgs()
        properties = self.handleFile(file_path)
        if enable_cp:
            alpha = 1 - cp_values
        else:
            alpha = 0.2
            cp_values = 0.8
        if enable_full:
            print("set full")
            pred_type = 'advance'
        else:
            print("set easy")
            pred_type = 'default'
        if len(properties) != 0:
            predict_results = list()
            index = 0
            for i in properties:
                pred_price, text = self.handleRequest(i, model_sel=model_sel, full=enable_full, alpha=alpha)
                predict_results.append({'id': index, 'price': pred_price, 'text': text, 'type': pred_type})
                index += 1
        else:
            predict_results = []
        return len(predict_results), predict_results, model_sel, cp_values

    def handleRequest(self, X, model_sel="RF", full=True, alpha=0.2):
        """
        Handle one request, this method is used by HandleNormalRequest, HandleProSingleRequest and HandleProBatchRequest.
        round the price to 100.
        :param X: numpy array, the features
        :param model_sel: str, the model selection, [RF, XGB, LGBM], default is RF.
        :param full: bool, set True to use full model.
        :param alpha: float, The alpha value for the CP predictor.
        :return: pred_price, text
        """
        print(full)
        if full:
            if model_sel == 'RF':
                pred_price = self.FullRFPredictor.PredictByX(X=X, ALPHA=alpha)
            elif model_sel == 'XGB':
                pred_price = self.FullXGBPredictor.PredictByX(X=X, ALPHA=alpha)
            elif model_sel == 'LGBM':
                pred_price = self.FullLGBMPredictor.PredictByX(X=X, ALPHA=alpha)
            else:
                pred_price = self.FullRFPredictor.PredictByX(X=X, ALPHA=alpha)
            text = self.FullDescriptor.GenerateDescription(X=X, predicted_price=pred_price['values'][0], full=full)
        else:
            if model_sel == 'RF':
                pred_price = self.EasyRFPredictor.PredictByX(X=X, ALPHA=alpha)
            elif model_sel == 'XGB':
                pred_price = self.EasyXGBPredictor.PredictByX(X=X, ALPHA=alpha)
            elif model_sel == 'LGBM':
                pred_price = self.EasyLGBMPredictor.PredictByX(X=X, ALPHA=alpha)
            else:
                pred_price = self.EasyRFPredictor.PredictByX(X=X, ALPHA=alpha)
            text = self.EasyDescriptor.GenerateDescription(X=X, predicted_price=pred_price['values'][0], full=full)
        print(f'use model: {model_sel}')
        print(pred_price)
        print(text)
        return f"{int(round(pred_price['values_range'][0], -2))}-{int(round(pred_price['values_range'][1], -2))}", text

    @staticmethod
    def handleFile(file_path):
        """
        Handle a file.
        :param file_path: file path to the csv file
        :return: numpy array of the csv file contents
        """
        if os.path.isfile(file_path):
            df = pd.read_csv(file_path)
            return df.to_numpy()
        else:
            return []

    def HandleRecordSearch(self, rID):
        """
        Handle a record search event.
        :param rID: str, the record ID
        :return: record_values, or None if the record does not exist.
        """
        record_values = self.RecordSearcher.SearchRecord(rID)
        if record_values is not None:
            pro_settings = record_values.get('status')
            pro_settings_str = f'enable_llm: {pro_settings[0]}, enable_full: {pro_settings[1]}, enable_cp: {pro_settings[2]}, cp_values: {pro_settings[3]}, enable_hidden: {pro_settings[4]}, model_sel: {pro_settings[5]}'
            features = record_values.get('features')
            price = record_values.get('price')
            description = record_values.get('text')
            rID = record_values.get('rID')
            model_sel = record_values.get('model_sel')
            confidence_level = record_values.get('confidence_level')
            if model_sel is None:
                model_sel = 'RF'
            if confidence_level is None:
                confidence_level = 0.8
            return {'status': True, 'values': [features, price, description, rID, pro_settings_str, model_sel, confidence_level]}
        else:
            return {'status': False, 'values': None}

    @staticmethod
    def DataPreprocessing(data_form, full):
        """
        Preprocess the input data.
        :param data_form: dict, the input data
        :param full: bool, set True to use full model.
        :return: numpy array of the preprocessed data
        """
        my_array = list()
        if full:
            for feature_name in Full_feature_names:
                if feature_name == 'bathrooms':
                    my_array.append(float(data_form.get('bathrooms')) / float(data_form.get('bedrooms')))
                elif feature_name == 'building_age':
                    # my_array.append(year - DecodeDate(data_form.get('yr_built')).getYear())
                    my_array.append(year - float(data_form.get('yr_built')))
                elif feature_name == 'renovated_year':
                    renovated_year = float(data_form.get('yr_renovated'))
                    if renovated_year == 0:
                        my_array.append(year - float(data_form.get('yr_built')))
                    else:
                        my_array.append(year - renovated_year)
                elif feature_name == 'year':
                    my_array.append(year)
                elif feature_name == 'month':
                    my_array.append(month)
                else:
                    my_array.append(float(data_form[feature_name]))
        else:
            for feature_name in Easy_feature_names:
                if feature_name == 'bathrooms':
                    my_array.append(float(data_form.get('bathrooms')) / float(data_form.get('bedrooms')))
                elif feature_name == 'building_age':
                    my_array.append(year - float(data_form.get('yr_built')))
                else:
                    my_array.append(float(data_form[feature_name]))
        return my_array

    @staticmethod
    def DataTrans(data_dict, data_class='default'):
        """
        Transform input data to features table
        :param data_dict: input data in dict
        :param data_class: 'default' or 'advance'
        :return: data in list of dict
        """
        res = list()
        for key, value in data_dict.items():
            row = dict()
            row['name'] = key
            if value != '':
                row['value'] = value
            else:
                row['value'] = "None"
            row['class'] = data_class
            res.append(row)
        return res

