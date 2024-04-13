from bson.json_util import loads
from .charts_controller import makeFoodGroupCharts, makeMealAdequacyChart
from .mealdata_controller import getFoodGroupsData , getMealStats, getMealStatsSex, getFoodGroupsDataSex

foodgroupcolors = {
"Animal-Sourced Protein" : "rgb(179, 36, 0)",
"Carbohydrate" : "rgb(255, 204, 102)",
"Combo Appetizer" : "rgb(218, 145, 1)", 
"Combo Dessert" : "rgb(255, 204, 255)",
"Combo Main Dish" : "rgb(204, 102, 0)",
"Dairy" : "rgb(255, 204, 153)",
"Fat" : "rgb(255, 153, 0)",
"Fruit" : "rgb(255, 77, 77)",
"Plant-Sourced Protein" : "rgb(153, 255, 102)",
"Rice" : "rgb(238, 238, 238)",
"Sugar" : "rgb(255, 217, 179)",
"Vegetable" : "rgb(115, 161, 69)",
}

#===========================================================================================================#

def getFoodGroupsDaily():
    df = getFoodGroupsData('daily')
    fig = makeFoodGroupCharts(df, "Count", "Food Group", "h", foodgroupcolors)

    return(loads(fig.to_json()))

def getFoodGroupsWeekly():
    df = getFoodGroupsData('weekly')
    fig = makeFoodGroupCharts(df, "Count", "Food Group", "h", foodgroupcolors)

    return(loads(fig.to_json()))

def getFoodGroupsMonthly():
    df = getFoodGroupsData('monthly')
    fig = makeFoodGroupCharts(df, "Count", "Food Group", "h", foodgroupcolors)
    
    return(loads(fig.to_json()))

#===========================================================================================================#

def getFoodGroupsDailySex(sex: str):
    df = getFoodGroupsDataSex(sex, 'daily')
    fig = makeFoodGroupCharts(df, "Count", "Food Group", "h", foodgroupcolors)

    return(loads(fig.to_json()))
 
def getFoodGroupsWeeklySex(sex: str):
    df = getFoodGroupsDataSex(sex, 'weekly')
    fig = makeFoodGroupCharts(df, "Count", "Food Group", "h", foodgroupcolors)

    return(loads(fig.to_json()))

def getFoodGroupsMonthlySex(sex: str):
    df = getFoodGroupsDataSex(sex, 'monthly')
    fig = makeFoodGroupCharts(df, "Count", "Food Group", "h", foodgroupcolors)
    
    return(loads(fig.to_json()))

#===========================================================================================================#

def getMealCountDaily():
    df = getMealStats('daily')
    charts = makeMealAdequacyChart(df)

    return charts

def getMealCountWeekly():
    df = getMealStats('weekly')
    charts = makeMealAdequacyChart(df)

    return charts

def getMealCountMonthly():
    df = getMealStats('monthly')
    charts = makeMealAdequacyChart(df)

    return charts

#===========================================================================================================#

def getMealCountDailySex(sex: str):
    df = getMealStatsSex(sex, 'daily')
    charts = makeMealAdequacyChart(df)

    return charts

def getMealCountWeeklySex(sex: str):
    df = getMealStatsSex(sex, 'weekly')
    charts = makeMealAdequacyChart(df)

    return charts

def getMealCountMonthlySex(sex: str):
    df = getMealStatsSex(sex, 'monthly')
    charts = makeMealAdequacyChart(df)

    return charts

#===========================================================================================================#