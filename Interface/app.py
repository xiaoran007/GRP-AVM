from flask import Flask, render_template, request, flash
import util

app = Flask(__name__)


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

if __name__ == '__main__':
    app.run()
