from flask import Flask, render_template, request

app = Flask(__name__)

def classify(message):
    return 'Spam'

@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        message = request.form.to_dict()
        message = list(message.values())
        result = classify(message)
        return render_template("result.html", prediction = result)

@app.route('/')
def index():
    return render_template('index.html')
