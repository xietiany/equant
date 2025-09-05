from lib.obj.stock import stock

def getInfo(ticker, period, valuationMethod, valationStage, growthHorizon, valuationHorizon, date):
    object = stock(ticker, period)
    data = {"error": ""}
    try:
        object.initialize(defaultRateApproach = True, valuationMethod = valuationMethod, defaultLTGrowth = False, \
                            valuationStage = valationStage, growthCalcHorizon = growthHorizon, \
                            valuationHorizon = valuationHorizon, date=date)
        data["valuationMethod"] = object.valuationMethod
        data["valuationStage"] = object.valuationStage
        data["startValue"] = object.starting
        data["growthCalcHorizon"] = object.growthCalcHorizon
        data["valuationHorizon"] = object.valuationHorizon
        data["firstStageGrowth"] = object.firstStageGrowthValue
        data["secondStageGrowth"] = object.secondStageGrowthValue
        data["LTGrowth"] = object.LTGrowth
        data["RR"] = object.RR
        data["FV"] = object.FV

    except ValueError as e:
        data["error"] = e

    return data

def getBacktestInfo(ticker, period, valuationMethod, valationStage, growthHorizon, valuationHorizon, startdate, enddate):
    object = stock(ticker, period)
    data = {"error": ""}
    try:
        object.backtesting(defaultRateApproach = True, valuationMethod = valuationMethod, defaultLTGrowth = False, \
                            valuationStage = valationStage, growthCalcHorizon = growthHorizon, \
                            valuationHorizon = valuationHorizon, start_date = startdate, end_date = enddate)
        data['backtestSwitch'] = True        
        data["res"] = object.getBacktestResult
        data["xaxis"] = object.getBacktestXaxis
        data["backtestDF"] = object.getBacktestingDF.to_html()

    except ValueError as e:
        data["error"] = e

    return data