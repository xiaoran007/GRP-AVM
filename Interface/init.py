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
        dependencies = ['torch', 'transformers', 'numpy', 'pandas', 'sklearn', 'xgboost', 'lightgbm', 'flask', 'mapie', 'joblib']
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

