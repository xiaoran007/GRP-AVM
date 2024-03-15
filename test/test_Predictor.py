import pytest
from model.Predictor import Predictor, CpPredictor
import model
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
        """
        Test the Init method.
        """
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
        """
        Test the Predict method.
        """
        def test_case1(self, case):
            x = case.get('full')
            predictor = Predictor(X=x, model_sel='RF', full=True, cwd=os.path.dirname(__file__))
            pred_dict = predictor.Predict()
            assert pred_dict['status'] == 0

        def test_case2(self, case):
            x = case.get('full')
            predictor = Predictor(X=x, model_sel='RF', full=False, cwd=os.path.dirname(__file__))
            pred_dict = predictor.Predict()
            assert pred_dict['status'] == 0

        def test_case3(self, case):
            x = case.get('normal')
            predictor = Predictor(X=x, model_sel='RF', full=False, cwd=os.path.dirname(__file__))
            pred_dict = predictor.Predict()
            assert pred_dict['status'] == 0

        def test_case4(self, case):
            x = case.get('normal')
            predictor = Predictor(X=x, model_sel='RF', full=True, cwd=os.path.dirname(__file__))
            pred_dict = predictor.Predict()
            assert pred_dict['status'] == -1

    class TestPredictByX:
        """
        Test the PredictByX method.
        """
        def test_Full(self, case):
            x = case.get('full')
            predictor = Predictor(X=None, model_sel='RF', full=True, cwd=os.path.dirname(__file__))
            pred_dict = predictor.PredictByX(X=x)
            assert pred_dict['status'] == 0

        def test_Easy(self, case):
            x = case.get('normal')
            predictor = Predictor(X=None, model_sel='RF', full=False, cwd=os.path.dirname(__file__))
            pred_dict = predictor.PredictByX(X=x)
            assert pred_dict['status'] == 0

    class TestNumpy2DF:
        """
        Test the Numpy2DF method.
        """
        def test_full2full(self, case):
            x = case.get('full')
            df = Predictor.numpy2df(x, full=True)
            assert df is not None

        def test_full2easy(self, case):
            x = case.get('full')
            df = Predictor.numpy2df(x, full=True)
            assert df is not None

        def test_easy2easy(self, case):
            x = case.get('normal')
            df = Predictor.numpy2df(x, full=False)
            assert df is not None

        def test_easy2full(self, case):
            x = case.get('normal')
            with pytest.raises(ValueError):
                Predictor.numpy2df(x, full=True)

    class TestLoadModel:
        def test_load(self):
            predictor = Predictor(X=None, model_sel='RF', full=True, cwd=os.path.dirname(__file__))
            os.chdir(os.path.dirname(model.__file__))
            predictor.model_sel = 'RF'
            assert predictor.LoadModel() is not None
            os.chdir(os.path.dirname(__file__))

        def test_unload(self):
            predictor = Predictor(X=None, model_sel='RF', full=True, cwd=os.path.dirname(__file__))
            os.chdir(os.path.dirname(model.__file__))
            predictor.model_sel = 'XGB'
            assert predictor.LoadModel() is None
            os.chdir(os.path.dirname(__file__))

    class TestCheckModel:
        """
        Test the CheckModel method.
        """
        def test_load(self):
            predictor = Predictor(X=None, model_sel='RF', full=True, cwd=os.path.dirname(__file__))
            assert predictor.CheckModel() is True

        def test_unload(self):
            predictor = Predictor(X=None, model_sel='XGB', full=True, cwd=os.path.dirname(__file__))
            assert predictor.CheckModel() is False



class TestCpPredictor:

    def test_predict(self):
        assert True


    def test_predict_by_x(slice_test_df):
        assert True


    def test_load_model(slice_test_df):
        assert True
