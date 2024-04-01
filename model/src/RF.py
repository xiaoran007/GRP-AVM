"""
Copyright (c) 2024 Tangtangfang Fang

All rights reserved.

This file is part of AVM-GRP.

AVM-GRP is distributed under the GPLv3 License.
See the LICENSE file at the top level of the distribution for details.
"""

import joblib


class RFModel(object):
    def __init__(self, lofi=False, lang=False):
        """
        :param lofi: Bool, set True if need easy model
        :param lang: Bool, set True if need descriptions
        """
        self.LOFI = lofi
        self.LANG = lang

    def Load(self):
        """
        :return: RF model object, None if fail
        """
        if self.LOFI:
            url = './object/RF_Easy.mdo'
        else:
            url = './object/RF_Full.mdo'
        try:
            RF_model = joblib.load(url)
            return RF_model
        except:
            return None


