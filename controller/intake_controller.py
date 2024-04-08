from .chartmaker_controller import makeAvgIntakeGraphs, makeIntakeHistograms 
from .intakedata_controller import getAvgIntakeDataWeek, getAvgIntakeData1Month, getAvgIntakeData3Month,  getIntakeCountDaily, getIntakeCountWeekly, getIntakeCountMonthly

def getAvgIntakeWeek():
    df = getAvgIntakeDataWeek()
    charts = makeAvgIntakeGraphs(df)

    return(charts)

def getAvgIntake1Month():
    df = getAvgIntakeData1Month()
    charts = makeAvgIntakeGraphs(df)

    return(charts)

def getAvgIntake3Month():
    df = getAvgIntakeData3Month()
    charts = makeAvgIntakeGraphs(df)

    return(charts)

def getIntakePlotDaily():
    df = getIntakeCountDaily()
    charts = makeIntakeHistograms(df)

    return charts

def getIntakePlotWeekly():
    df = getIntakeCountWeekly()
    charts = makeIntakeHistograms(df)

    return charts

def getIntakePlotMonthly():
    df = getIntakeCountMonthly() 
    charts = makeIntakeHistograms(df)

    return charts