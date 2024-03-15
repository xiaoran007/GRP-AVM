import joblib
import os
from RFBuilder import RFBuilder
from XGBBuilder import XGBBuilder
from LGBMBuilder import LGBMBuilder
from CPBuilder import CPBuilder


class Builder(object):
    def __init__(self, full, cp):
        self.FULL = full
        self.CP = cp
        self.init()

    def buildRF(self):
        if self.CP:
            rf = RFBuilder.Make(self.FULL)
            model = CPBuilder(pre_fit_model=rf).Make(self.FULL)
        else:
            model = RFBuilder.Make(self.FULL)
        self.saveModel(model, f'RF_{self.generateName()}')

    def buildXGB(self):
        if self.CP:
            xgb = XGBBuilder.Make(self.FULL)
            model = CPBuilder(pre_fit_model=xgb).Make(self.FULL)
        else:
            model = XGBBuilder.Make(self.FULL)
        self.saveModel(model, f'XGB_{self.generateName()}')

    def buildLGBM(self):
        if self.CP:
            lgbm = LGBMBuilder.Make(self.FULL)
            model = CPBuilder(pre_fit_model=lgbm).Make(self.FULL)
        else:
            model = LGBMBuilder.Make(self.FULL)
        self.saveModel(model, f'LGBM_{self.generateName()}')

    @staticmethod
    def init():
        if os.path.exists('./target'):
            pass
        else:
            os.mkdir('./target')

    @staticmethod
    def saveModel(model, name):
        print(f'Save model to ./target/{name}.mdo')
        joblib.dump(model, f'./target/{name}.mdo')
        print("Save OK.")

    def generateName(self):
        if self.CP:
            res = "CP_"
        else:
            res = ""
        if self.FULL:
            res = res + "Full"
        else:
            res = res + "Easy"
        return res


def buildAll():
    for i in [True, False]:
        for j in [True, False]:
            builder = Builder(full=i, cp=j)
            builder.buildRF()
            builder.buildXGB()
            builder.buildLGBM()


buildAll()
