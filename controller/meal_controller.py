from bson.json_util import loads
from .chartmaker_controller import makeFoodGroupBar, makeFoodHistograms, makeAvgMealGraphs
from .mealdata_controller import getFoodGroupsData , getMealStats, getMealStatsSex, getFoodGroupsDataSex

#===========================================================================================================#

def getFoodGroupsDaily():
    df = getFoodGroupsData('daily')
    fig = makeFoodGroupBar(df, "Count", "Food Group", "h", "Food Group")

    return(loads(fig.to_json()))

def getFoodGroupsWeekly():
    df = getFoodGroupsData('weekly')
    fig = makeFoodGroupBar(df, "Count", "Food Group", "h", "Food Group")

    return(loads(fig.to_json()))

def getFoodGroupsMonthly():
    df = getFoodGroupsData('monthly')
    fig = makeFoodGroupBar(df, "Count", "Food Group", "h", "Food Group")
    
    return(loads(fig.to_json()))

#===========================================================================================================#

def getFoodGroupsDailySex(sex: str):
    df = getFoodGroupsDataSex(sex, 'daily')
    fig = makeFoodGroupBar(df, "Count", "Food Group", "h", "Food Group")

    return(loads(fig.to_json()))
 
def getFoodGroupsWeeklySex(sex: str):
    df = getFoodGroupsDataSex(sex, 'weekly')
    fig = makeFoodGroupBar(df, "Count", "Food Group", "h", "Food Group")

    return(loads(fig.to_json()))

def getFoodGroupsMonthlySex(sex: str):
    df = getFoodGroupsDataSex(sex, 'monthly')
    fig = makeFoodGroupBar(df, "Count", "Food Group", "h", "Food Group")
    
    return(loads(fig.to_json()))

#===========================================================================================================#

def getMealCountDaily():
    df = getMealStats('daily')
    charts = makeFoodHistograms(df)

    return charts

def getMealCountWeekly():
    df = getMealStats('weekly')
    charts = makeFoodHistograms(df)

    return charts

def getMealCountMonthly():
    df = getMealStats('monthly')
    charts = makeFoodHistograms(df)

    return charts

#===========================================================================================================#

def getMealCountDailySex(sex: str):
    df = getMealStatsSex(sex, 'daily')
    charts = makeFoodHistograms(df)

    return charts

def getMealCountWeeklySex(sex: str):
    df = getMealStatsSex(sex, 'weekly')
    charts = makeFoodHistograms(df)

    return charts

def getMealCountMonthlySex(sex: str):
    df = getMealStatsSex(sex, 'monthly')
    charts = makeFoodHistograms(df)

    return charts

#===========================================================================================================#