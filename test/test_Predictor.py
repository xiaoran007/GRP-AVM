"""
Copyright (c) 2024 Tangtangfang Fang

All rights reserved.

This file is part of AVM-GRP.

AVM-GRP is distributed under the GPLv3 License.
See the LICENSE file at the top level of the distribution for details.
"""

import pytest
from model.Predictor import Predictor, CpPredictor
import model
import os
import numpy


class TestPredictor:
    """
    Test the Predictor class.
    """

    @pytest.fixture(scope='class')
    def case(self):
        res = dict()
        res['normal'] = numpy.array([3, 1.5, 1500, 6337, 61, 47.7276, -122.312])
        res['full'] = numpy.array(
            [4, 2.5, 1950, 7350, 1.0, 0, 0, 3, 7, 1150, 800, 51, 51, 47.656, -122.134, 2050, 9068, 2014, 12])
        return res

    class TestInit:
        """
        Test the Init method.
        """

        def test_full_init(self):
            predictor = Predictor(X=None, model_sel='RF', full=True, cwd=os.path.dirname(__file__))
            assert predictor is not None

        def test_easy_init(self):
            predictor = Predictor(X=None, model_sel='RF', full=False, cwd=os.path.dirname(__file__))
            assert predictor is not None

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


class TestCpPredictor:
    """
    Test the CpPredictor class.
    """

    @pytest.fixture(scope='class')
    def case(self):
        res = dict()
        res['normal'] = numpy.array([3, 1.5, 1500, 6337, 61, 47.7276, -122.312])
        res['full'] = numpy.array(
            [4, 2.5, 1950, 7350, 1.0, 0, 0, 3, 7, 1150, 800, 51, 51, 47.656, -122.134, 2050, 9068, 2014, 12])
        return res

    class TestInit:
        """
        Test the Init method.
        """

        def test_rf_f(self):
            predictor = CpPredictor(X=None, model_sel='RF', full=True, cwd=os.path.dirname(__file__), alpha=0.2)
            assert predictor is not None

        def test_xgb_f(self):
            predictor = CpPredictor(X=None, model_sel='XGB', full=True, cwd=os.path.dirname(__file__), alpha=0.2)
            assert predictor is not None

        def test_lgbm_f(self):
            predictor = CpPredictor(X=None, model_sel='LGBM', full=True, cwd=os.path.dirname(__file__), alpha=0.2)
            assert predictor is not None

        def test_rf_e(self):
            predictor = CpPredictor(X=None, model_sel='RF', full=False, cwd=os.path.dirname(__file__), alpha=0.2)
            assert predictor is not None

        def test_xgb_e(self):
            predictor = CpPredictor(X=None, model_sel='XGB', full=False, cwd=os.path.dirname(__file__), alpha=0.2)
            assert predictor is not None

        def test_lgbm_e(self):
            predictor = CpPredictor(X=None, model_sel='LGBM', full=False, cwd=os.path.dirname(__file__), alpha=0.2)
            assert predictor is not None

    class TestPredict:
        """
        Test the Predict method.
        """

        def test_rf_ff(self, case):
            x = case.get('full')
            predictor = CpPredictor(X=x, model_sel='RF', full=True, cwd=os.path.dirname(__file__), alpha=0.2)
            assert predictor.Predict().get('status') == 0

        def test_rf_ee(self, case):
            x = case.get('normal')
            predictor = CpPredictor(X=x, model_sel='RF', full=False, cwd=os.path.dirname(__file__), alpha=0.2)
            assert predictor.Predict().get('status') == 0

        def test_rf_fe(self, case):
            x = case.get('full')
            predictor = CpPredictor(X=x, model_sel='RF', full=False, cwd=os.path.dirname(__file__), alpha=0.2)
            assert predictor.Predict().get('status') == 0

        def test_rf_ef(self, case):
            x = case.get('normal')
            predictor = CpPredictor(X=x, model_sel='RF', full=True, cwd=os.path.dirname(__file__), alpha=0.2)
            assert predictor.Predict().get('status') == -1

        def test_xgb_ff(self, case):
            x = case.get('full')
            predictor = CpPredictor(X=x, model_sel='XGB', full=True, cwd=os.path.dirname(__file__), alpha=0.2)
            assert predictor.Predict().get('status') == 0

        def test_xgb_ee(self, case):
            x = case.get('normal')
            predictor = CpPredictor(X=x, model_sel='XGB', full=False, cwd=os.path.dirname(__file__), alpha=0.2)
            assert predictor.Predict().get('status') == 0

        def test_xgb_fe(self, case):
            x = case.get('full')
            predictor = CpPredictor(X=x, model_sel='XGB', full=False, cwd=os.path.dirname(__file__), alpha=0.2)
            assert predictor.Predict().get('status') == 0

        def test_xgb_ef(self, case):
            x = case.get('normal')
            predictor = CpPredictor(X=x, model_sel='XGB', full=True, cwd=os.path.dirname(__file__), alpha=0.2)
            assert predictor.Predict().get('status') == -1

        def test_lgbm_ff(self, case):
            x = case.get('full')
            predictor = CpPredictor(X=x, model_sel='LGBM', full=True, cwd=os.path.dirname(__file__), alpha=0.2)
            assert predictor.Predict().get('status') == 0

        def test_lgbm_ee(self, case):
            x = case.get('normal')
            predictor = CpPredictor(X=x, model_sel='LGBM', full=False, cwd=os.path.dirname(__file__), alpha=0.2)
            assert predictor.Predict().get('status') == 0

        def test_lgbm_fe(self, case):
            x = case.get('full')
            predictor = CpPredictor(X=x, model_sel='LGBM', full=False, cwd=os.path.dirname(__file__), alpha=0.2)
            assert predictor.Predict().get('status') == 0

        def test_lgbm_ef(self, case):
            x = case.get('normal')
            predictor = CpPredictor(X=x, model_sel='LGBM', full=True, cwd=os.path.dirname(__file__), alpha=0.2)
            assert predictor.Predict().get('status') == -1

    class TestPredictByX:
        """
        Test the PredictByX method.
        """

        def test_f1(self, case):
            x = case.get('full')
            predictor = CpPredictor(X=None, model_sel='RF', full=True, cwd=os.path.dirname(__file__), alpha=0.2)
            assert predictor.PredictByX(X=x, ALPHA=0.2).get('status') == 0

        def test_f2(self, case):
            x = case.get('full')
            predictor = CpPredictor(X=None, model_sel='RF', full=True, cwd=os.path.dirname(__file__), alpha=0.2)
            assert predictor.PredictByX(X=x, ALPHA=0.8).get('status') == 0

        def test_e1(self, case):
            x = case.get('normal')
            predictor = CpPredictor(X=None, model_sel='RF', full=False, cwd=os.path.dirname(__file__), alpha=0.2)
            assert predictor.PredictByX(X=x, ALPHA=0.2).get('status') == 0

        def test_e2(self, case):
            x = case.get('normal')
            predictor = CpPredictor(X=None, model_sel='RF', full=False, cwd=os.path.dirname(__file__), alpha=0.2)
            assert predictor.PredictByX(X=x, ALPHA=0.8).get('status') == 0

    class TestLoadModel:
        """
        Test the LoadModel method.
        """

        def test_rf_f(self):
            predictor = CpPredictor(X=None, cwd=os.path.dirname(__file__))
            os.chdir(os.path.dirname(model.__file__))
            predictor.model_sel = 'RF'
            predictor.FULL = True
            assert predictor.LoadModel() is not None
            os.chdir(os.path.dirname(__file__))

        def test_rf_e(self):
            predictor = CpPredictor(X=None, cwd=os.path.dirname(__file__))
            os.chdir(os.path.dirname(model.__file__))
            predictor.model_sel = 'RF'
            predictor.FULL = False
            assert predictor.LoadModel() is not None
            os.chdir(os.path.dirname(__file__))

        def test_xgb_f(self):
            predictor = CpPredictor(X=None, cwd=os.path.dirname(__file__))
            os.chdir(os.path.dirname(model.__file__))
            predictor.model_sel = 'XGB'
            predictor.FULL = True
            assert predictor.LoadModel() is not None
            os.chdir(os.path.dirname(__file__))

        def test_xgb_e(self):
            predictor = CpPredictor(X=None, cwd=os.path.dirname(__file__))
            os.chdir(os.path.dirname(model.__file__))
            predictor.model_sel = 'XGB'
            predictor.FULL = False
            assert predictor.LoadModel() is not None
            os.chdir(os.path.dirname(__file__))

        def test_lgbm_f(self):
            predictor = CpPredictor(X=None, cwd=os.path.dirname(__file__))
            os.chdir(os.path.dirname(model.__file__))
            predictor.model_sel = 'LGBM'
            predictor.FULL = True
            assert predictor.LoadModel() is not None
            os.chdir(os.path.dirname(__file__))

        def test_lgbm_e(self):
            predictor = CpPredictor(X=None, cwd=os.path.dirname(__file__))
            os.chdir(os.path.dirname(model.__file__))
            predictor.model_sel = 'LGBM'
            predictor.FULL = False
            assert predictor.LoadModel() is not None
            os.chdir(os.path.dirname(__file__))
