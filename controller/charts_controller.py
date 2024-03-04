from bson.json_util import loads
from .chartmaker_controller import makeFoodGroupBar, makeAvgIntakeGraphs, makeHistograms
from .chartdata_controller import getFoodGroupsDataDaily, getFoodGroupsDataWeekly, getFoodGroupsDataMonthly, getAvgIntakeData1Month, getAvgIntakeData3Month, getAvgIntakeData6Month, getAvgIntakeData1Year, getIntakeCountDaily, getIntakeCountWeekly, getIntakeCountMonthly

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
    data = makeAvgIntakeGraphs(df)

    return(data)

def getAvgIntake3Month():
    df = getAvgIntakeData3Month()
    data = makeAvgIntakeGraphs(df)

    return(data)

def getAvgIntake6Month():
    df = getAvgIntakeData6Month()
    data = makeAvgIntakeGraphs(df)

    return(data)

def getAvgIntake1Year():
    df = getAvgIntakeData1Year()
    data = makeAvgIntakeGraphs(df)

    return(data)

def getIntakeCountDaily():
    df = getIntakeCountDaily()
    data = makeHistograms(df)

    return data

def getIntakeCountWeekly():
    df = getIntakeCountWeekly()
    data = makeHistograms(df)

    return data

def getIntakeCountMonthly():
    df = getIntakeCountMonthly() 
    data = makeHistograms(df)

    return data

