from NLGen.Descriptor import Descriptor
from Datasets.Data import Default, Default_Easy
from model.Predictor import Predictor, CpPredictor
import os


Full_feature_names = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view',
                            'condition',
                            'grade',
                            'sqft_above', 'sqft_basement', 'building_age', 'renovated_year', 'lat', 'long',
                            'sqft_living15',
                            'sqft_lot15', 'year', 'month']

Easy_feature_names = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'building_age', 'lat', 'long']
year = 2014
month = 6


def backend(data_array, full):
    predictor = CpPredictor(data_array, model_sel='RF', full=full, alpha=0.2, cwd=os.path.dirname(__file__))
    pred_price = predictor.Predict()
    print(pred_price)
    descriptor = Descriptor(data_array, pred_price['values'][0], full=full, cwd=os.path.dirname(__file__))
    text = descriptor.GetDescription()
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


class DecodeDate(object):
    def __init__(self, date_str):
        self.DATE = date_str
        self.YEAR, self.MONTH, self.DAY = DecodeDate.decode_date(self.DATE)

    @staticmethod
    def decode_date(date_str):
        context = date_str.split('-')
        return int(context[0]), int(context[1]), int(context[2])

    def getYear(self):
        return self.YEAR

    def getMonth(self):
        return self.MONTH

    def getDay(self):
        return self.DAY
