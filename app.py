from flask import Flask
from flask import request
from flask import render_template
import sys
import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend
import matplotlib.pyplot as plt
sys.path.append("/Users/tianyixie/Documents/equant") 
from model import getInfo, getBacktestInfo
import requests
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def stockBoard():
    if request.method == 'POST':
        if 'valuation' in request.form:
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
        elif 'backtest' in request.form:
            ticker = request.form['ticker']
            period = request.form['period']
            valuationMethod = request.form['valuationMethod']
            valuationStage = request.form['valuationStage']
            growthHorizon = request.form['growthHorizon']
            valuationHorizon = request.form['valuationHorizon']
            startdate = request.form['startdate']
            enddate = request.form['enddate']

            data = getBacktestInfo(ticker, period, valuationMethod, valuationStage, int(growthHorizon), int(valuationHorizon), startdate, enddate)
            # label = ["fair value", "top 10 mean", "mean"]
            # for i in range(len(label)):
            #     val = [float(x[i]) for x in data["res"]]
            #     x = data["xaxis"]
            #     plt.plot(x, val) # For a line plot with markers
            plt.plot(data["xaxis"], data["res"], label = ["fair value", "top 10 mean", "mean"], marker='o', linestyle='-') # For a line plot with markers
        
            plt.xticks(rotation=90)
            plt.xlabel("X-axis")
            plt.ylabel("Y-axis")
            plt.title("Plot of Backtesting")
            plt.legend()
            plt.grid(True)
            
            plt.savefig('static/backtest.png') # design the valution function

        return render_template("index.html", plot_url = 'static/backtest.png', **data)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=8080)