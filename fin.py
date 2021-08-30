from flask import Flask, render_template, request
import json
from difflib import get_close_matches
from app import translate_app

filename = 'data.json'
data = json.load(open(filename))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        word = str(request.form['words'])
        # glucose = int(request.form['glucose'])
        # bp = int(request.form['bloodpressure'])
        # st = int(request.form['skinthickness'])
        # insulin = int(request.form['insulin'])
        # bmi = float(request.form['bmi'])
        # dpf = float(request.form['dpf'])
        # age = int(request.form['age'])

        # data = np.array([[word]])
        my_prediction = translate_app(word)

        return render_template('result.html', prediction=my_prediction, word=word, len=len(my_prediction),
                               tpy=type(my_prediction))


if __name__ == '__main__':
    app.run(debug=True)
