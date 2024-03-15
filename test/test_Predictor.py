import pytest
from model.Predictor import Predictor, CpPredictor
import os
import numpy


class TestPredictor:
    @pytest.fixture(scope='class')
    def case(self):
        res = dict()
        res['normal'] = numpy.array([3, 1.5, 1500, 6337, 61, 47.7276, -122.312])
        res['full'] = numpy.array([4, 2.5, 1950, 7350, 1.0, 0, 0, 3, 7, 1150, 800, 51, 51, 47.656, -122.134, 2050, 9068, 2014, 12])
        return res

    class TestInit:
        def test_case1(self):
            predictor = Predictor(X=None, model_sel='RF', full=True, cwd=os.path.dirname(__file__))
            assert predictor is not None

        def test_case2(self):
            predictor = Predictor(X=None, model_sel='XGB', full=True, cwd=os.path.dirname(__file__))
            assert predictor is not None

        def test_case3(self):
            predictor = Predictor(X=None, model_sel='LGBM', full=True, cwd=os.path.dirname(__file__))
            assert predictor is not None

        def test_case4(self):
            predictor = Predictor(X=None, model_sel='RF', full=False, cwd=os.path.dirname(__file__))
            assert predictor is not None

        def test_case5(self):
            predictor = Predictor(X=None, model_sel='XGB', full=False, cwd=os.path.dirname(__file__))
            assert predictor is not None

        def test_case6(self):
            predictor = Predictor(X=None, model_sel='LGBM', full=False, cwd=os.path.dirname(__file__))
            assert predictor is not None

    class TestPredict:
        def test_case1(self, case):
            x = case.get('full')
            predictor = Predictor(X=x, model_sel='RF', full=True, lang=False, cwd=os.path.dirname(__file__))
            pred_dict = predictor.Predict()
            assert pred_dict['status'] == 0

        def test_case2(self, case):
            x = case.get('full')
            predictor = Predictor(X=x, model_sel='RF', full=False, lang=False, cwd=os.path.dirname(__file__))
            pred_dict = predictor.Predict()
            assert pred_dict['status'] == 0

        def test_case3(self, case):
            x = case.get('normal')
            predictor = Predictor(X=x, model_sel='RF', full=False, lang=False, cwd=os.path.dirname(__file__))
            pred_dict = predictor.Predict()
            assert pred_dict['status'] == 0

        def test_case4(self, case):
            x = case.get('normal')
            predictor = Predictor(X=x, model_sel='RF', full=True, lang=False, cwd=os.path.dirname(__file__))
            pred_dict = predictor.Predict()
            assert pred_dict['status'] == -1


    class TestPredictByX:
        def test_case1(self):
            assert True

    class TestNumpy2DF:

        def test_case1(self):
            assert self.i == 5

    class TestLoadModel:
        def test_case1(self):
            assert True

    class TestCheckModel:
        def test_case1(self):
            assert True



class TestCpPredictor:

    def test_predict(self):
        assert True


    def test_predict_by_x(slice_test_df):
        assert True


    def test_load_model(slice_test_df):
        assert True
