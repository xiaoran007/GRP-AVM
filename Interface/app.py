import sys
sys.path.append("../")
sys.path.append("./")
import joblib
from flask import Flask, render_template, request, flash, g, redirect, url_for, session
import util
import json

app = Flask(__name__,   static_url_path='',
            static_folder='static',
            template_folder='templates')
app.secret_key = 'my_secret_key'

print("Loading model...")
backendHandler = util.BackendEventHandler()
print("Init ok!")


@app.route('/', methods=['GET', 'POST'])
def pro_mode():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        return "undefined"



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
        features, pred_price, text = backendHandler.HandleNormalRequest(form_dict=session.get('normal_form_basic'), full=False, alpha=0.2)
        print(f"OK\nPrice: {pred_price}\nText: {text}")
        return render_template('normalModeFormEnd.html', features=features, price=pred_price, description=text, price_pred=pred_price)
    # from pro
    elif request.method == 'POST':
        session['normal_form_pro'] = request.form.to_dict()
        combined = {**session.get('normal_form_basic'), **(session.get('normal_form_pro'))}
        features, pred_price, text = backendHandler.HandleNormalRequest(form_dict=combined,
                                                                        full=True, alpha=0.2)
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
        features, pred_price, text, rID_str, model_sel, confidence_level = backendHandler.HandleProSingleRequest(form_dict=request_dict)
        return render_template('proModeSingleResult.html', features=features, price=pred_price, description=text, rID=rID_str, model_sel=model_sel, confidence_level=confidence_level)


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
        result = backendHandler.HandleRecordSearch(rID=request.form.get('rID'))
        if result.get('status'):
            features, price, description, rID, pro_settings_str, model_sel, confidence_level = result.get('values')
            return render_template('proModeRecordResult.html', features=features, price=price, description=description, rID=rID, pro_settings=pro_settings_str, model_sel=model_sel, confidence_level=confidence_level)
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
            results_len, results, model_sel, confidence_level = backendHandler.HandleProBatchRequest(request.form.to_dict(), save_path + user_file.filename)
            return render_template('proModeBatchResult.html', lens=results_len, results=results, model_sel=model_sel, confidence_level=confidence_level)
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
