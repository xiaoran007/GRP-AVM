import os
import json


class Init(object):
    def __init__(self):
        pass

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

