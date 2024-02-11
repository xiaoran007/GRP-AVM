from model.src import RF


class Predictor(object):

    def __init__(self, X, model_sel="RF", lofi=False, lang=False):
        """
        :param X: dataframe, 19 columns if lofi is False, 7 columns if lofi is True
        :param model_sel: string, model type, support 'RF'
        :param lofi: Bool, set True if need easy model
        :param lang: Bool, set True if need descriptions
        """
        self.X = X
        self.model_sel = model_sel
        self.LOFI = lofi
        self.LANG = lang
        self.MODEL = self.LoadModel()

    def Predict(self):
        """
        :return: dict, key 'status' 0 if success, key 'values' contents return values
        """
        if self.CheckModel():
            try:
                return_dict = dict()
                predicted_values = self.MODEL.predict(self.X)
                return_dict['status'] = 0
                return_dict['values'] = predicted_values.tolist()
                return return_dict
            except:
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
        if self.model_sel == 'RF':
            return RF.RFModel(self.LOFI, self.LANG).Load()

    def CheckModel(self):
        """
        :return: Bool, True if model already loaded
        """
        if self.MODEL is None:
            return False
        else:
            return True





