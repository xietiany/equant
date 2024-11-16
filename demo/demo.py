from flask import Flask
from flask import request
from flask import render_template
import requests
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def stock():
    if request.method == 'POST':
        ticker = request.form['ticker']
        url = f"https://financialmodelingprep.com/api/v3/ratios/{ticker}?period=quarter&apikey=5MGyRLKiJleTCG8AOx26iYV6z8B9enmP"
        response = requests.get(url)
        data = response.json()

        return render_template("index.html", data = data)
    
    return render_template("index.html")