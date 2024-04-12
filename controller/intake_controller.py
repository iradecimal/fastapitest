from .chartmaker_controller import makeAvgIntakeGraphs, makeIntakeHistograms 
from .intakedata_controller import getIntakeCount, getIntakeCountSex

# def getAvgIntakeWeek():
#     df = getAvgIntakeDataWeek()
#     charts = makeAvgIntakeGraphs(df)

#     return(charts)

# def getAvgIntake1Month():
#     df = getAvgIntakeData1Month()
#     charts = makeAvgIntakeGraphs(df)

#     return(charts)

# def getAvgIntake3Month():
#     df = getAvgIntakeData3Month()
#     charts = makeAvgIntakeGraphs(df)

#     return(charts)

def getIntakePlotDaily():
    df = getIntakeCount("daily")
    charts = makeIntakeHistograms(df)

    return charts

def getIntakePlotWeekly():
    df = getIntakeCount("weekly")
    charts = makeIntakeHistograms(df)

    return charts

def getIntakePlotMonthly():
    df = getIntakeCount("monthly") 
    charts = makeIntakeHistograms(df)

    return charts

def getIntakePlotDailySex(sex: str):
    df = getIntakeCountSex(sex, "daily")
    charts = makeIntakeHistograms(df)

    return charts

def getIntakePlotWeeklySex(sex: str):
    df = getIntakeCountSex(sex, "weekly")
    charts = makeIntakeHistograms(df)

    return charts

def getIntakePlotMonthlySex(sex: str):
    df = getIntakeCountSex(sex, "monthly") 
    charts = makeIntakeHistograms(df)

    return charts

