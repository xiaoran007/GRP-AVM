"""
Copyright (c) 2024 Tangtangfang Fang

All rights reserved.

This file is part of AVM-GRP.

AVM-GRP is distributed under the GPLv3 License.
See the LICENSE file at the top level of the distribution for details.
"""

import pytest
from NLGen.Descriptor import Descriptor
import NLGen
import os
import numpy


class TestDescriptor:
    """
    Test the Descriptor class.
    """

    @pytest.fixture(scope='class')
    def case(self):
        res = dict()
        res['normal_x'] = numpy.array([3, 1.5, 1500, 6337, 61, 47.7276, -122.312])
        res['full_x'] = numpy.array(
            [4, 2.5, 1950, 7350, 1.0, 0, 0, 3, 7, 1150, 800, 51, 51, 47.656, -122.134, 2050, 9068, 2014, 12])
        res['normal_price'] = 50000
        res['full_price'] = 100000
        return res

    class TestInit:
        """
        Test the init method.
        """

        def test_full_init(self):
            descriptor = Descriptor(X=None, predicted_price=None, full=True, cwd=os.path.dirname(__file__))
            assert descriptor is not None

        def test_easy_init(self):
            descriptor = Descriptor(X=None, predicted_price=None, full=False, cwd=os.path.dirname(__file__))
            assert descriptor is not None

    class TestLoadObject:
        """
        Test the LoadObject method.
        """

        def test_load(self):
            descriptor = Descriptor(X=None, predicted_price=None, full=True, cwd=os.path.dirname(__file__))
            os.chdir(os.path.dirname(NLGen.__file__))
            descriptor.LoadObject()
            os.chdir(os.path.dirname(__file__))

    class TestGenerateDescription:
        """
        Test the GenerateDescription method.
        """

        def test_normal(self, case):
            descriptor = Descriptor(X=None, predicted_price=None, full=False, cwd=os.path.dirname(__file__))
            description = descriptor.GenerateDescription(X=case.get('normal_x'),
                                                         predicted_price=case.get('normal_price'), full=False)
            assert description != "Description not generated."

        def test_full(self, case):
            descriptor = Descriptor(X=None, predicted_price=None, full=True, cwd=os.path.dirname(__file__))
            description = descriptor.GenerateDescription(X=case.get('full_x'), predicted_price=case.get('full_price'),
                                                         full=True)
            assert description != "Description not generated."

    class TestGeneratePosAndCons:
        """
        Test the GeneratePosAndCons method.
        """

        def test_normal(self, case):
            descriptor = Descriptor(X=None, predicted_price=None, full=False, cwd=os.path.dirname(__file__))
            descriptor.X = case.get('normal_x')
            descriptor.PRICE = case.get('normal_price')
            descriptor.FULL = False
            pos_cons_dict = descriptor.generatePosAndCons()
            assert pos_cons_dict['status'] is True

        def test_unloaded(self, case):
            descriptor = Descriptor(X=None, predicted_price=None, full=False, cwd=os.path.dirname(__file__))
            descriptor.X = case.get('normal_x')
            descriptor.PRICE = case.get('normal_price')
            descriptor.FULL = False
            descriptor.AVG = None
            descriptor.KMEANS = None
            pos_cons_dict = descriptor.generatePosAndCons()
            assert pos_cons_dict['status'] is False

    class TestNumpy2Df:
        """
        Test the Numpy2Df method.
        """

        def test_full2full(self, case):
            x = case.get('full_x')
            df = Descriptor.numpy2df(x, full=True)
            assert df is not None

        def test_full2easy(self, case):
            x = case.get('full_x')
            df = Descriptor.numpy2df(x, full=True)
            assert df is not None

        def test_easy2easy(self, case):
            x = case.get('normal_x')
            df = Descriptor.numpy2df(x, full=False)
            assert df is not None

        def test_easy2full(self, case):
            x = case.get('normal_x')
            with pytest.raises(ValueError):
                Descriptor.numpy2df(x, full=True)
