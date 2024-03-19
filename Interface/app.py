from init import Init
print("Init dependencies")
Init.initDependencies()
import sys
sys.path.append("../")
sys.path.append("./")
from flask import Flask, render_template, request, session, send_file
import util

app = Flask(__name__,   static_url_path='',
            static_folder='static',
            template_folder='templates')
app.secret_key = 'my_secret_key'
print("Init path")
Init.initPath()
print("Init app")
Init.initApp()
Init.initObjectFiles()
print("Loading model...")
backendHandler = util.BackendEventHandler()
print("Init ok!")


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    This method handles all requests to the root URL (/).
    Support: GET
    :param: request
    :return: response
    """
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        return "undefined"


@app.route('/indev', methods=['GET', 'POST'])
def indev():
    """
    This method handle all requests to the indev URL (/indev).
    Support: GET
    :param: request
    :return: response
    """
    if request.method == 'GET':
        return render_template('indev.html')
    elif request.method == 'POST':
        return "undefined"


@app.route('/readmore', methods=['GET', 'POST'])
def readmore():
    """
    This method handle all requests to the readmore URL (/readmore).
    Support: GET
    :param: request
    :return: response
    """
    if request.method == 'GET':
        return render_template('readmore.html')
    elif request.method == 'POST':
        return "undefined"


@app.route('/getstarted', methods=['GET', 'POST'])
def getstarted():
    """
    This method handle all requests to the getstarted URL (/getstarted).
    Support: GET
    :param: request
    :return: response
    """
    if request.method == 'GET':
        return render_template('getStartPage.html')
    elif request.method == 'POST':
        return "undefined"


@app.route('/normal_mode_form', methods=['GET', 'POST'])
def normal_mode_form():
    """
    This method handle all requests to the normal_mode_form URL (/normal_mode_form).
    Support: GET
    :param: request
    :return: response
    """
    if request.method == 'GET':
        return render_template('normalModeFormBasic.html')
    elif request.method == 'POST':
        return "undefined"


@app.route('/normal_mode_mid', methods=['POST'])
def normal_mode_mid():
    """
    This method handle all requests to the normal_mode_mid URL (/normal_mode_mid).
    Support: POST
    :param: request
    :return: response
    """
    if request.method == 'POST':
        print(request.form)
        session['normal_form_basic'] = request.form.to_dict()
        return render_template('normalModeFormMid.html')


@app.route('/normal_mode_pro', methods=['GET', 'POST'])
def normal_mode_pro():
    """
    This method handle all requests to the normal_mode_pro URL (/normal_mode_pro).
    Support: GET
    :param: request
    :return: response
    """
    if request.method == 'GET':
        print(f"from share {session.get('normal_form_basic')}")
        return render_template('normalModeFormPro.html')
    elif request.method == 'POST':
        return "undefined"


@app.route('/normal_mode_end', methods=['GET', 'POST'])
def normal_mode_end():
    """
    This method handle all requests to the normal_mode_end URL (/normal_mode_end).
    Support: GET, POST
    :param: request
    :return: response
    """
    # from basic
    if request.method == 'GET':
        if not util.InputCheckEventHandler(full=False, pro=False, batch=False, form_dict=session.get('normal_form_basic')).HandleEvent():
            return render_template('normalModeInputError.html')
        else:
            features, pred_price, text = backendHandler.HandleNormalRequest(form_dict=session.get('normal_form_basic'), full=False, alpha=0.2)
            print(f"OK\nPrice: {pred_price}\nText: {text}")
            return render_template('normalModeFormEnd.html', features=features, price=pred_price, description=text, price_pred=pred_price, rID='Normal')
    # from pro
    elif request.method == 'POST':
        session['normal_form_pro'] = request.form.to_dict()
        combined = {**session.get('normal_form_basic'), **(session.get('normal_form_pro'))}
        print(combined)
        if not util.InputCheckEventHandler(full=True, pro=False, batch=False, form_dict=combined).HandleEvent():
            return render_template('normalModeInputError.html')
        else:
            features, pred_price, text = backendHandler.HandleNormalRequest(form_dict=combined,
                                                                            full=True, alpha=0.2)
            print(f"OK\nPrice: {pred_price}\nText: {text}")
            return render_template('normalModeFormEnd.html', features=features, price=pred_price, description=text, price_pred=pred_price, rID='Normal')


@app.route('/pro_mode_start', methods=['GET', 'POST'])
def pro_mode_start():
    """
    This method handle all requests to the pro_mode_start URL (/pro_mode_start).
    Support: GET
    :param: request
    :return: response
    """
    if request.method == 'GET':
        return render_template('proModeStart.html')
    elif request.method == 'POST':
        return "undefined"


@app.route('/pro_mode_form', methods=['GET', 'POST'])
def pro_mode_form():
    """
    This method handle all requests to the pro_mode_form URL (/pro_mode_form).
    Support: GET
    :param: request
    :return: response
    """
    if request.method == 'GET':
        return render_template('proModeForm.html')
    elif request.method == 'POST':
        return "undefined"


@app.route('/pro_mode_single', methods=['GET', 'POST'])
def pro_mode_single():
    """
    This method handle all requests to the pro_mode_single URL (/pro_mode_single).
    Support: POST
    :param: request
    :return: response
    """
    if request.method == 'GET':
        return render_template('proModeInputError.html')
    elif request.method == 'POST':
        request_dict = request.form.to_dict()
        if not util.InputCheckEventHandler(full=True, pro=True, batch=False, form_dict=request_dict).HandleEvent():
            return render_template('proModeInputError.html')
        else:
            features, pred_price, text, rID_str, model_sel, confidence_level, rID = backendHandler.HandleProSingleRequest(form_dict=request_dict)
            return render_template('proModeSingleResult.html', features=features, price=pred_price,
                                   description=text, rID_str=rID_str, model_sel=model_sel, confidence_level=confidence_level, rID=rID)


@app.route('/pro_mode_record_search', methods=['GET', 'POST'])
def pro_mode_record_search():
    """
    This method handle all requests to the pro_mode_record_search URL (/pro_mode_record_search).
    Support: GET
    :param: request
    :return: response
    """
    if request.method == 'GET':
        return render_template('proModeRecordSearch.html')
    elif request.method == 'POST':
        return "undefined"


@app.route('/pro_mode_record_result', methods=['GET', 'POST'])
def pro_mode_record_result():
    """
    This method handle all requests to the pro_mode_record_result URL (/pro_mode_record_result).
    Support: POST
    :param: request
    :return: response
    """
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
    """
    This method handle all requests to the pro_mode_batch URL (/pro_mode_batch).
    Support: GET
    :param: request
    :return: response
    """
    if request.method == 'GET':
        return render_template('proModeBatch.html')
    elif request.method == 'POST':
        return "undefined"


@app.route('/pro_mode_batch_upload', methods=['GET', 'POST'])
def pro_mode_batch_upload():
    """
    This method handle all requests to the pro_mode_batch_upload URL (/pro_mode_batch_upload).
    Support: POST
    :param: request
    :return: response
    """
    if request.method == 'GET':
        return "undefined"
    elif request.method == 'POST':
        if 'file' in request.files and request.files['file'].filename != '' and request.files['file']:
            user_file = request.files['file']
            save_path = './upload/'
            user_file.save(save_path + user_file.filename)
            if not util.InputCheckEventHandler(full=True, pro=True, batch=True, form_dict=request.form.to_dict()).HandleEvent():
                return render_template('proModeBatchError.html')
            else:
                try:
                    results_len, results, model_sel, confidence_level = backendHandler.HandleProBatchRequest(request.form.to_dict(), save_path + user_file.filename)
                    return render_template('proModeBatchResult.html', lens=results_len, results=results, model_sel=model_sel, confidence_level=confidence_level)
                except Exception as e:
                    print("Error: ", e)
                    return render_template('proModeBatchError.html')
        else:
            return render_template('proModeBatchError.html')


@app.route('/download_result', methods=['GET', 'POST'])
def download_result():
    """
    This method handle all requests to the download_result URL (/download_result).
    Support: POST
    :param: request
    :return: response
    """
    if request.method == 'GET':
        return "undefined"
    elif request.method == 'POST':
        rID = request.form.get('rID')
        file_path = f'./sent/{rID}.pdf'
        file_name = f'rID{rID}.pdf'
        return send_file(file_path, as_attachment=True, download_name=file_name)


@app.route('/temp', methods=['GET', 'POST'])
def temp():
    """
    This method handle all requests to the temp URL (/temp).
    Support: GET
    :param: request
    :return: response
    """
    if request.method == 'GET':
        return render_template('temp.html')
    elif request.method == 'POST':
        return "undefined"


if __name__ == '__main__':
    app.run(debug=True)
