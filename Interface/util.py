import time
from NLGen.Descriptor import Descriptor
from Datasets.Data import Default, Default_Easy
from model.Predictor import Predictor, CpPredictor
import os
import json
import pandas as pd

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
    def __init__(self):
        pass

    @staticmethod
    def generateID():
        current_time = str(int(time.time()))
        time_id = current_time[-6:]
        return time_id

    def checkIfRecordExists(rID):
        rec_list = json.load(open('records/rec.json', 'r'))
        if rID in rec_list:
            return True
        else:
            return False


class ProSettingsEventHandler(object):
    """
    handler for pro settings
    """
    def __init__(self, request_dict):
        """

        :param request_dict: request form in dict
        """
        self.requestDict = request_dict

    def getControlArgs(self):
        """

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
    def __init__(self):
        pass


def backend(data_array, full):
    predictor = CpPredictor(data_array, model_sel='RF', full=full, alpha=0.2, cwd=os.path.dirname(__file__))
    pred_price = predictor.Predict()
    print(pred_price)
    descriptor = Descriptor(data_array, pred_price['values'][0], full=full, cwd=os.path.dirname(__file__))
    text = descriptor.generateDescription()
    print(text)
    return f"{pred_price['values_range'][0]}-{pred_price['values_range'][1]}", text


def data_preprocessing(data_form, full):
    my_array = list()
    if full is True:
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
    elif full is False:
        for feature_name in Easy_feature_names:
            if feature_name == 'bathrooms':
                my_array.append(float(data_form.get('bathrooms')) / float(data_form.get('bedrooms')))
            elif feature_name == 'building_age':
                my_array.append(year - float(data_form.get('yr_built')))
            else:
                my_array.append(float(data_form[feature_name]))
    return my_array


def data_trans(data_dict, data_class):
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


def get_control_args(request_dict):
    """

    :param request_dict: request type in dictionary
    :return: list of control args
    """
    if request_dict.get('llm') is not None:
        enable_llm = True
    else:
        enable_llm = False
    if request_dict.get('full') is not None:
        enable_full = True
    else:
        enable_full = False
    if request_dict.get('cp') is not None:
        enable_cp = True
        cp_values = float(request_dict.get('cp_value'))
    else:
        enable_cp = False
        cp_values = 0.0
    if request_dict.get('hidden') is not None:
        enable_hidden = True
    else:
        enable_hidden = False
    if request_dict.get('model') is not None:
        model_sel = request_dict.get('model')
    else:
        model_sel = 'RF'
    return enable_llm, enable_full, enable_cp, cp_values, enable_hidden, model_sel


def generateID():
    current_time = str(int(time.time()))
    time_id = current_time[-6:]
    return time_id


def checkIfRecordExists(rID):
    rec_list = json.load(open('records/rec.json', 'r'))
    if rID in rec_list:
        return True
    else:
        return False


def handleFile(file_path):
    """

    :param file_path: file path to the csv file
    :return: numpy array of the csv file contents
    """
    if os.path.isfile(file_path):
        df = pd.read_csv(file_path)
        return df.to_numpy()
    else:
        return []

