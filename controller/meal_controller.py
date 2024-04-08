from bson.json_util import loads
from .chartmaker_controller import makeFoodGroupBar, makeFoodHistograms, makeAvgMealGraphs
from .mealdata_controller import getFoodGroupsDataDaily, getFoodGroupsDataWeekly, getFoodGroupsDataMonthly, getMealStatsDaily, getMealStatsMonthly, getMealStatsWeekly, getMealAvgWeekly, getMealAvgMonthly

def getFoodGroupsDaily():
    df = getFoodGroupsDataDaily()
    fig = makeFoodGroupBar(df, "Count", "Food Group", "h", "Food Group")

    return(loads(fig.to_json()))

def getFoodGroupsWeekly():
    df = getFoodGroupsDataWeekly()
    fig = makeFoodGroupBar(df, "Count", "Food Group", "h", "Food Group")

    return(loads(fig.to_json()))

def getFoodGroupsMonthly():
    df = getFoodGroupsDataMonthly()
    fig = makeFoodGroupBar(df, "Count", "Food Group", "h", "Food Group")
    
    return(loads(fig.to_json()))

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

def getMealAvgWeekly():
    df = getMealAvgWeekly()
    charts = makeAvgMealGraphs(df)

    return charts

def getMealAvgWeekly():
    df = getMealAvgMonthly()
    charts = makeAvgMealGraphs(df)

    return charts