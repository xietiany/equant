from flask import Flask
from flask import request
from flask import render_template
import sys
sys.path.append("/Users/tianyixie/Documents/equant") 
from model import getInfo
import requests
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def stockBoard():
    if request.method == 'POST':
        ticker = request.form['ticker']
        period = request.form['period']
        valuationMethod = request.form['valuationMethod']
        valuationStage = request.form['valuationStage']
        growthHorizon = request.form['growthHorizon']
        valuationHorizon = request.form['valuationHorizon']
        date = request.form['date']
        # url = f"https://financialmodelingprep.com/api/v3/ratios/{ticker}?period=quarter&apikey=5MGyRLKiJleTCG8AOx26iYV6z8B9enmP"
        # response = requests.get(url)
        # data = response.json()

        data = getInfo(ticker, period, valuationMethod, valuationStage, int(growthHorizon), int(valuationHorizon), date) # design the valution function
        
        print(data)
        return render_template("index.html", **data)
    return render_template("index.html")