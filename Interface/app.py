from flask import Flask, render_template, request, flash, g, redirect, url_for, session
import util

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
        return request.form


@app.route('/temp', methods=['GET', 'POST'])
def temp():
    if request.method == 'GET':
        return render_template('temp.html')
    elif request.method == 'POST':
        return "undefined"


if __name__ == '__main__':
    app.run(debug=True)
