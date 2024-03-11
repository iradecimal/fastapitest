from bson.json_util import loads
from .chartmaker_controller import makeFoodGroupBar, makeAvgIntakeGraphs, makeIntakeHistograms, makeFoodHistograms 
from .chartdata_controller import getFoodGroupsDataDaily, getFoodGroupsDataWeekly, getFoodGroupsDataMonthly, getAvgIntakeData1Month, getAvgIntakeData3Month, getAvgIntakeData6Month, getIntakeCountDaily, getIntakeCountWeekly, getIntakeCountMonthly, getMealStatsDaily, getMealStatsMonthly, getMealStatsWeekly


def getFoodGroupsDaily():
    df = getFoodGroupsDataDaily()
    fig = makeFoodGroupBar(df, "Count", "Food Group", "h", "Food Group", "Food Groups", "Count")

    return(loads(fig.to_json()))

def getFoodGroupsWeekly():
    df = getFoodGroupsDataWeekly()
    fig = makeFoodGroupBar(df, "Count", "Food Group", "h", "Food Group", "Food Groups", "Count")

    return(loads(fig.to_json()))

def getFoodGroupsMonthly():
    df = getFoodGroupsDataMonthly()
    fig = makeFoodGroupBar(df, "Count", "Food Group", "h", "Food Group", "Food Groups", "Count")
    
    return(loads(fig.to_json()))

def getAvgIntake1Month():
    df = getAvgIntakeData1Month()
    charts = makeAvgIntakeGraphs(df)

    return(charts)

def getAvgIntake3Month():
    df = getAvgIntakeData3Month()
    charts = makeAvgIntakeGraphs(df)

    return(charts)

def getAvgIntake6Month():
    df = getAvgIntakeData6Month()
    charts = makeAvgIntakeGraphs(df)

    return(charts)

def getIntakeCountDaily():
    df = getIntakeCountDaily()
    charts = makeIntakeHistograms(df)

    return charts

def getIntakeCountWeekly():
    df = getIntakeCountWeekly()
    charts = makeIntakeHistograms(df)

    return charts

def getIntakeCountMonthly():
    df = getIntakeCountMonthly() 
    charts = makeIntakeHistograms(df)

    return charts

def getMealCountDaily():
    df = getMealStatsDaily()
    charts = makeFoodHistograms(df)

    return charts

def getMealCountWeekly():
    df = getMealStatsWeekly()
    charts = makeFoodHistograms(df)

    return charts

def getMealCountMonthly():
    df = getMealStatsMonthly()
    charts = makeFoodHistograms(df)

    return charts