import joblib
from flask import Flask, render_template, request, flash, g, redirect, url_for, session
import util
import json

app = Flask(__name__,   static_url_path='',
            static_folder='static',
            template_folder='templates')
app.secret_key = 'my_secret_key'


@app.route('/', methods=['GET', 'POST'])
def pro_mode():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        return "undefined"


@app.route('/result', methods=['POST'])
def pro_result():
    if request.method == 'POST':
        print(request.form)
        ar = util.data_preprocessing(request.form, full=True)
        print(ar)
        pred_price, text = util.backend(ar, full=True)
        return f"OK\nPrice: {pred_price}\nText: {text}"


@app.route('/indev', methods=['GET', 'POST'])
def indev():
    if request.method == 'GET':
        return render_template('indev.html')
    elif request.method == 'POST':
        return "undefined"


@app.route('/readmore', methods=['GET', 'POST'])
def readmore():
    if request.method == 'GET':
        return render_template('readmore.html')
    elif request.method == 'POST':
        return "undefined"


@app.route('/getstarted', methods=['GET', 'POST'])
def getstarted():
    if request.method == 'GET':
        return render_template('getStartPage.html')
    elif request.method == 'POST':
        return "undefined"


@app.route('/normal_mode_form', methods=['GET', 'POST'])
def normal_mode_form():
    if request.method == 'GET':
        return render_template('normalModeFormBasic.html')
    elif request.method == 'POST':
        return "undefined"


@app.route('/normal_mode_mid', methods=['POST'])
def normal_mode_mid():
    if request.method == 'POST':
        print(request.form)
        session['normal_form_basic'] = request.form.to_dict()
        return render_template('normalModeFormMid.html')


@app.route('/normal_mode_pro', methods=['GET', 'POST'])
def normal_mode_pro():
    if request.method == 'GET':
        print(f"from share {session.get('normal_form_basic')}")
        return render_template('normalModeFormPro.html')
    elif request.method == 'POST':
        return "undefined"


@app.route('/normal_mode_end', methods=['GET', 'POST'])
def normal_mode_end():
    # from basic
    if request.method == 'GET':
        print(f"from share {session.get('normal_form_basic')}")
        features = util.data_trans(session.get('normal_form_basic'), 'default')
        ar = util.data_preprocessing(session.get('normal_form_basic'), full=False)
        print(ar)
        pred_price, text = util.backend(ar, full=False)
        print(f"OK\nPrice: {pred_price}\nText: {text}")
        return render_template('normalModeFormEnd.html', features=features, price=pred_price, description=text, price_pred=pred_price)
    # from pro
    elif request.method == 'POST':
        print(request.form)
        session['normal_form_pro'] = request.form.to_dict()
        print(f"from share basic: {session.get('normal_form_basic')}")
        print(f"from share pro: {session.get('normal_form_pro')}")
        combined = {**session.get('normal_form_basic'), **(session.get('normal_form_pro'))}
        print(combined)
        features = util.data_trans(combined, 'advance')
        ar = util.data_preprocessing(combined, full=True)
        print(ar)
        pred_price, text = util.backend(ar, full=True)
        print(f"OK\nPrice: {pred_price}\nText: {text}")
        return render_template('normalModeFormEnd.html', features=features, price=pred_price, description=text, price_pred=pred_price)


@app.route('/pro_mode_start', methods=['GET', 'POST'])
def pro_mode_start():
    if request.method == 'GET':
        return render_template('proModeStart.html')
    elif request.method == 'POST':
        return "undefined"


@app.route('/pro_mode_form', methods=['GET', 'POST'])
def pro_mode_form():
    if request.method == 'GET':
        return render_template('proModeForm.html')
    elif request.method == 'POST':
        return "undefined"


@app.route('/pro_mode_single', methods=['GET', 'POST'])
def pro_mode_single():
    if request.method == 'GET':
        return render_template('proModeSingleResult.html')
    elif request.method == 'POST':
        request_dict = request.form.to_dict()
        enable_llm, enable_full, enable_cp, cp_values, enable_hidden, model_sel = util.get_control_args(request_dict)
        if enable_hidden:
            rID = '******'
            rID_str = 'This prediction will not be recorded.'
        else:
            rID = util.generateID()
            rID_str = f"Result ID is {rID}"
        if enable_full:
            features = util.data_trans(request_dict, 'advance')
            ar = util.data_preprocessing(request_dict, full=True)
            print(ar)
            pred_price, text = util.backend(ar, full=True)
            print(f"OK\nPrice: {pred_price}\nText: {text}")
            if not enable_hidden:
                rec_list = json.load(open('records/rec.json', 'r'))
                joblib.dump({'rID': rID, 'status': [enable_llm, enable_full, enable_cp, cp_values, enable_hidden, model_sel], 'features': features, 'price': pred_price, 'text': text}, f'./records/{rID}.record')
                rec_list.append(rID)
                json.dump(rec_list, open('records/rec.json', 'w'))
            return render_template('proModeSingleResult.html', features=features, price=pred_price, description=text,
                                   rID=rID_str)
        else:
            features = util.data_trans(request_dict, 'default')
            ar = util.data_preprocessing(request_dict, full=False)
            print(ar)
            pred_price, text = util.backend(ar, full=False)
            print(f"OK\nPrice: {pred_price}\nText: {text}")
            if not enable_hidden:
                rec_list = json.load(open('records/rec.json', 'r'))
                joblib.dump({'rID': rID, 'status': [enable_llm, enable_full, enable_cp, cp_values, enable_hidden, model_sel], 'features': features, 'price': pred_price, 'text': text},
                        f'./records/{rID}.record')
                rec_list.append(rID)
                json.dump(rec_list, open('records/rec.json', 'w'))
            return render_template('proModeSingleResult.html', features=features, price=pred_price, description=text,
                                   rID=rID_str)


@app.route('/pro_mode_record_search', methods=['GET', 'POST'])
def pro_mode_record_search():
    if request.method == 'GET':
        return render_template('proModeRecordSearch.html')
    elif request.method == 'POST':
        return "undefined"


@app.route('/pro_mode_record_result', methods=['GET', 'POST'])
def pro_mode_record_result():
    if request.method == 'GET':
        return "undefined"
    elif request.method == 'POST':
        record_id = request.form.get('rID')
        if util.checkIfRecordExists(record_id):
            record_values = joblib.load(f'./records/{record_id}.record')
            pro_settings = record_values.get('status')
            pro_settings_str = f'enable_llm: {pro_settings[0]}, enable_full: {pro_settings[1]}, enable_cp: {pro_settings[2]}, cp_values: {pro_settings[3]}, enable_hidden: {pro_settings[4]}, model_sel: {pro_settings[5]}'
            return render_template('proModeRecordResult.html', features=record_values.get('features'), price=record_values.get('price'), description=record_values.get('text'),
                                   rID=record_values.get('rID'), pro_settings=f'{pro_settings_str}')
        else:
            return render_template('proModeNoSuchRecord.html')


@app.route('/pro_mode_batch', methods=['GET', 'POST'])
def pro_mode_batch():
    if request.method == 'GET':
        return render_template('proModeBatch.html')
    elif request.method == 'POST':
        return "undefined"


@app.route('/pro_mode_batch_upload', methods=['GET', 'POST'])
def pro_mode_batch_upload():
    if request.method == 'GET':
        return "undefined"
    elif request.method == 'POST':
        if 'file' in request.files and request.files['file'].filename != '' and request.files['file']:
            user_file = request.files['file']
            save_path = './upload/'
            user_file.save(save_path + user_file.filename)
            file_contents_list = util.handleFile(save_path + user_file.filename)
            request_dict = request.form.to_dict()
            enable_llm, enable_full, enable_cp, cp_values, enable_hidden, model_sel = util.get_control_args(
                request_dict)
            if enable_full:
                if len(file_contents_list) != 0:
                    predict_results = list()
                    index = 0
                    for i in file_contents_list:
                        pred_price, text = util.backend(i, full=True)
                        predict_results.append({'id': index, 'price': pred_price, 'text': text, 'type': 'advance'})
                        index += 1
                else:
                    predict_results = []
            else:
                if len(file_contents_list) != 0:
                    predict_results = list()
                    index = 0
                    for i in file_contents_list:
                        pred_price, text = util.backend(i, full=False)
                        predict_results.append({'id': index, 'price': pred_price, 'text': text, 'type': 'default'})
                        index += 1
                else:
                    predict_results = []
            return render_template('proModeBatchResult.html', lens=len(file_contents_list), results=predict_results)
        else:
            return render_template('proModeBatchError.html')


@app.route('/temp', methods=['GET', 'POST'])
def temp():
    if request.method == 'GET':
        return render_template('temp.html')
    elif request.method == 'POST':
        return "undefined"


if __name__ == '__main__':
    app.run(debug=True)
