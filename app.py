from flask import Flask, request, render_template
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from model import getInfo, getBacktestInfo

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def stockBoard():
    if request.method == 'POST':
        if 'valuation' in request.form:
            ticker = request.form['ticker']
            period = request.form['period']
            valuationMethod = request.form['valuationMethod']
            valuationStage = request.form['valuationStage']
            growthHorizon = int(request.form['growthHorizon'])
            valuationHorizon = int(request.form['valuationHorizon'])
            date = request.form['date']
            data = getInfo(ticker, period, valuationMethod, valuationStage, growthHorizon, valuationHorizon, date)
            return render_template("index.html", formType='valuation', **data)

        elif 'backtest' in request.form:
            ticker = request.form['ticker']
            period = request.form['period']
            valuationMethod = request.form['valuationMethod']
            valuationStage = request.form['valuationStage']
            growthHorizon = int(request.form['growthHorizon'])
            valuationHorizon = int(request.form['valuationHorizon'])
            startdate = request.form['startdate']
            enddate = request.form['enddate']
            data = getBacktestInfo(ticker, period, valuationMethod, valuationStage, growthHorizon, valuationHorizon, startdate, enddate)

            fig, ax = plt.subplots(figsize=(12, 5))
            ax.plot(data["xaxis"], data["res"], label=["fair value", "top 10 mean", "mean"], marker='o', linestyle='-')
            ax.set_xlabel("Date")
            ax.set_ylabel("Price")
            ax.set_title("Backtesting Results")
            ax.legend()
            ax.grid(True, alpha=0.3)
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            fig.savefig('static/backtest.png', dpi=150, bbox_inches='tight')
            plt.close(fig)

            return render_template("index.html", formType='backtest', plot_url='static/backtest.png', **data)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=8080)
