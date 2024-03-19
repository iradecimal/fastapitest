from bson.json_util import loads
from .chartmaker_controller import makeFoodGroupBar, makeAvgIntakeGraphs, makeIntakeHistograms, makeFoodHistograms 
from .chartdata_controller import getFoodGroupsDataDaily, getFoodGroupsDataWeekly, getFoodGroupsDataMonthly, getAvgIntakeDataWeek, getAvgIntakeData1Month, getAvgIntakeData3Month,  getIntakeCountDaily, getIntakeCountWeekly, getIntakeCountMonthly, getMealStatsDaily, getMealStatsMonthly, getMealStatsWeekly


def getFoodGroupsDaily():
    df = getFoodGroupsDataDaily()
    fig = makeFoodGroupBar(df, "Count", "Food Group", "h", "Food Group", "Food Groups")

    return(loads(fig.to_json()))

def getFoodGroupsWeekly():
    df = getFoodGroupsDataWeekly()
    fig = makeFoodGroupBar(df, "Count", "Food Group", "h", "Food Group", "Food Groups")

    return(loads(fig.to_json()))

def getFoodGroupsMonthly():
    df = getFoodGroupsDataMonthly()
    fig = makeFoodGroupBar(df, "Count", "Food Group", "h", "Food Group", "Food Groups")
    
    return(loads(fig.to_json()))

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
    print(df)
    charts = makeFoodHistograms(df)

    return charts