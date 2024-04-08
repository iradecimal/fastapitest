from bson.json_util import loads
from .sexdata_controller import getIntakeAvgSexWeekly, getIntakeAvgSexMonthly, getIntakeCountSexWeekly, getIntakeCountSexMonthly
from .sexmaker_controller import makeIntakeSexHistograms, makeAvgIntakeSexGraphs

def getSexIntakeCountWeekly():
    df = getIntakeCountSexWeekly()
    charts = makeIntakeSexHistograms(df)
    
    return(charts) 

def getSexIntakeCountMonthly():
    df = getIntakeCountSexMonthly()
    charts = makeIntakeSexHistograms(df)
    
    return(charts)  

def getSexAvgIntakeWeekly():
    df = getIntakeAvgSexWeekly()
    charts = makeAvgIntakeSexGraphs(df)

    return(charts) 

def getSexAvgIntakeMonthly():
    df = getIntakeAvgSexMonthly()    
    charts = makeAvgIntakeSexGraphs(df)

    return(charts) 