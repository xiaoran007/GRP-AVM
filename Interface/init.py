import os
import json
import importlib.util
import platform
import time


class Init(object):
    def __init__(self):
        pass

    @staticmethod
    def initDependencies():
        not_found = []
        dependencies = ['torch', 'transformers', 'numpy', 'pandas', 'sklearn', 'xgboost', 'lightgbm', 'flask', 'mapie',
                        'joblib']
        os_name = platform.system()
        if os_name == "Windows":
            print("Running on Windows, init dependencies")
            dependencies.append('pdfkit')
        else:
            print("Running on Unix, init dependencies")
            dependencies.append('weasyprint')
        for i in dependencies:
            if importlib.util.find_spec(i) is None:
                not_found.append(i)
                print(f"Check module {i} not found.")
            else:
                print(f"Check module {i} pass.")
        if len(not_found) != 0:
            print(f'Dependencies not found: {not_found}')
            exit(1)
        else:
            print('Dependencies pass.')
            print('------------------')

    @staticmethod
    def initApp():
        if os.path.exists('./sent'):
            pass
        else:
            os.mkdir('./sent')
            print('created sent')

        if os.path.exists('./records'):
            if os.path.exists('./records/rec.json'):
                try:
                    with open('./records/rec.json', 'r') as f:
                        json.load(f)
                except json.JSONDecodeError:
                    print('Empty file')
                    with open('./records/rec.json', 'w') as f:
                        json.dump([], f)
                    print('created rec.json')
        else:
            os.mkdir('./records')
            print('created records')
            with open('./records/rec.json', 'w') as f:
                json.dump([], f)
            print('created rec.json')
        print('init done')
        print('---------')

    @staticmethod
    def initObjectFiles():
        not_found = []
        model_object_files = ['object/rev311/LGBM_CP_Easy.mdo',
                              'object/rev311/LGBM_CP_Full.mdo',
                              'object/rev311/RF_CP_Easy.mdo',
                              'object/rev311/RF_CP_Full.mdo',
                              'object/rev311/XGB_CP_Easy.mdo',
                              'object/rev311/XGB_CP_Full.mdo']
        model_path_prefix = '../model/'
        class_object_files = ['class/class_avg_Easy.mdo',
                              'class/class_avg_Full.mdo',
                              'class/kmeans_model.mdo',
                              'class/kmeans_model_Easy.mdo',
                              'class/kmeans_model_Full.mdo']
        class_path_prefix = '../NLGen/'
        print('Check model object files')
        for i in model_object_files:
            if not os.path.exists(model_path_prefix + i):
                print(f"Check model object file {i} not found.")
                not_found.append(model_path_prefix + i)
            else:
                print(f"Check model object file {i} pass.")
        print(f'Check class object files')
        for i in class_object_files:
            if not os.path.exists(class_path_prefix + i):
                print(f"Check class object file {i} not found.")
                not_found.append(class_path_prefix + i)
            else:
                print(f"Check class object file {i} pass.")
        if len(not_found) != 0:
            print(f'Object files not found: {not_found}')
            exit(1)
        else:
            print('Object files pass.')
            print('------------------')
