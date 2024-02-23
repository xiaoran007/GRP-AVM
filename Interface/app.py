from flask import Flask, render_template, request, flash
import util

app = Flask(__name__,   static_url_path='',
            static_folder='static',
            template_folder='templates')


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
        return render_template('normalModeForm.html')
    elif request.method == 'POST':
        return "undefined"


if __name__ == '__main__':
    app.run(debug=True)
