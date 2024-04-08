from db import intakes, meals
from datetime import date, datetime, timedelta
import pandas as pd
from pymongoarrow.api import Schema

# Schemas shared between several functions
FoodGroupsSchema = Schema({'_id': str, 'count': int})
FoodCountSchema = Schema({'fat': float, 'carbs': float, 'proteins': float, 'cal': float, 'waste': float})
FoodAvgSchema = Schema({'_id': str, 'fat': float, 'carbs': float, 'proteins': float, 'cal': float, 'waste': float})

foodgroup = {'$group': {
    '_id': '$foodgroups', 
    'count': {'$sum': 1}
}}

avgmealgroup = {'$group' : {
           '_id' :{ '$dateToString': { 'format': "%Y-%m-%d", 'date': "$datetime"} },
            'fat': {'$avg': '$fat'},
            'carbs': {'$avg': '$carbs'},
            'proteins': {'$avg': '$proteins'},
            'cal': {'$avg': '$cal'},
            'waste': {'$avg': '$waste'},
        }}

foodcountproject = { '$project': {
            'fat': '$fat',
            'carbs': '$carbs',
            'proteins': '$proteins',
            'cal': '$cal',
            'waste': '$waste',
}}

def getDatetimeInterval(interval: str):
    #dateToday = datetime.today()
    dateToday = date.fromisoformat("2023-11-23")
    datetimeToday = datetime.fromisoformat(dateToday.isoformat())
    datetimeBefore = ''
    if interval == "daily":
        datetimeBefore = datetimeToday - timedelta(days=1)
    elif interval == "weekly":
        datetimeBefore = datetimeToday - timedelta(weeks=1)
    elif interval == "monthly":
        datetimeBefore = datetimeToday - timedelta(weeks=4)
    elif interval == "3month":
        datetimeBefore = datetimeToday - timedelta(weeks=12)
    else:
        raise ValueError("Wrong interval was sent. Please check for capitalization/spelling errors.")
    datetimeinterval = { '$match': {'datetime': { '$lte': datetimeToday, '$gte': datetimeBefore}}} 
    return datetimeinterval


def getFoodGroupsDataDaily():
    pipeline = [
        getDatetimeInterval("daily"),  
        {'$unwind': '$foodgroups'}, foodgroup
    ]
    df = (meals.aggregate_pandas_all(pipeline, schema = FoodGroupsSchema))
    df = df.rename(columns={'_id': 'Food Group', 'count': 'Count'})

    return df

def getFoodGroupsDataWeekly():
    pipeline = [
        getDatetimeInterval("weekly"),    
        {'$unwind': '$foodgroups'}, foodgroup
    ]
    df = (meals.aggregate_pandas_all(pipeline,  schema = FoodGroupsSchema))
    df = df.rename(columns={'_id': 'Food Group', 'count': 'Count'})

    return df

def getFoodGroupsDataMonthly():
    pipeline = [
        getDatetimeInterval("monthly"),
        {'$unwind': '$foodgroups'}, foodgroup
    ]
    df = (meals.aggregate_pandas_all(pipeline,  schema = FoodGroupsSchema))
    df = df.rename(columns={'_id': 'Food Group', 'count': 'Count'})

    return(df)

def getMealStatsDaily():
    pipeline = [
        getDatetimeInterval("daily"),  
        foodcountproject
    ]

    return(meals.aggregate_pandas_all(pipeline, schema = FoodCountSchema))

def getMealStatsWeekly():
    pipeline = [
        getDatetimeInterval("weekly"),    
        foodcountproject
    ]

    return(meals.aggregate_pandas_all(pipeline, schema = FoodCountSchema))

def getMealStatsMonthly():
    pipeline = [
        getDatetimeInterval("monthly"),   
        foodcountproject
    ]

    return(meals.aggregate_pandas_all(pipeline, schema = FoodCountSchema))

def getMealAvgWeekly():
    pipeline = [
        getDatetimeInterval("weekly"),   
        avgmealgroup
    ]
    df = meals.aggregate_pandas_all(pipeline, schema = FoodAvgSchema)
    df = df.rename(columns={'_id': 'date'})

    return(df)

def getMealAvgMonthly():
    pipeline = [
        getDatetimeInterval("monthly"),   
        avgmealgroup
    ]
    df = meals.aggregate_pandas_all(pipeline, schema = FoodAvgSchema)
    df = df.rename(columns={'_id': 'date'})

    return(df)