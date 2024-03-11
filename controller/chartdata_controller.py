from db import intakes, meals
from datetime import date, datetime, timedelta
import pandas as pd
from pymongoarrow.api import Schema

# Schemas shared between several functions
FoodGroupsSchema = Schema({'_id': str, 'count': int})
AvgIntakeSchema = Schema({'_id': str, 'waterglass': float, 'sleephrs': float, 'dailycal': float, 'steps': float})
IntakeCountSchema =Schema({'waterglass': float, 'sleephrs': float, 'dailycal': float, 'steps': float})
FoodCountSchema = Schema({'fat': float, 'carbs': float, 'proteins': float, 'cal': float, 'waste': float})

foodgroup = {'$group': {
    '_id': '$foodgroups', 
    'count': {'$sum': 1}
}}

avgintakegroup = {'$group': {
    '_id': '$date',
    'steps': {'$avg': '$steps'},
    'sleephrs': {'$avg': '$sleephrs'},
    'waterglass': {'$avg': '$waterglass'},
    'dailycal': {'$avg': '$dailycal'},
}}

intakecountproject = {'$project': {
    "waterglass": "$waterglass",
    "sleephrs": "$sleephrs",
    "dailycal": "$dailycal",
    "steps": "$steps",
}}

foodcountproject = { '$project': {
            'fat': '$fat',
            'carbs': '$carbs',
            'proteins': '$proteins',
            'cal': '$cal',
            'waste': '$waste',
        }}

def getFoodGroupsDataDaily():
    #dateToday = datetime.today()
    dateToday = date.fromisoformat("2023-11-23")
    datetimeToday = datetime.fromisoformat(dateToday.isoformat())
    datetimeYesterday = datetimeToday - timedelta(days=1)
    pipeline = [
        { '$match': {'datetime': { '$lte': datetimeToday, '$gte': datetimeYesterday}}},  
        {'$unwind': '$foodgroups'}, foodgroup
    ]
    df = (meals.aggregate_pandas_all(pipeline, schema = FoodGroupsSchema))
    df = df.rename(columns={'_id': 'Food Group', 'count': 'Count'})

    return df

def getFoodGroupsDataWeekly():
    #dateToday = datetime.today()
    dateToday = date.fromisoformat("2023-11-23")
    datetimeToday = datetime.fromisoformat(dateToday.isoformat())
    datetimeLastWeek = datetimeToday - timedelta(days=7)
    pipeline = [
        { '$match': {'datetime': { '$lte': datetimeToday, '$gte': datetimeLastWeek}}},    
        {'$unwind': '$foodgroups'}, foodgroup
    ]
    df = (meals.aggregate_pandas_all(pipeline,  schema = FoodGroupsSchema))
    df = df.rename(columns={'_id': 'Food Group', 'count': 'Count'})

    return df

def getFoodGroupsDataMonthly():
    #dateToday = datetime.today()
    dateToday = date.fromisoformat("2023-11-23")
    datetimeToday = datetime.fromisoformat(dateToday.isoformat())
    datetimeLastMonth = datetimeToday - timedelta(weeks=10)
    pipeline = [
        { '$match': {'datetime': { '$lte': datetimeToday, '$gte': datetimeLastMonth}}}, 
        {'$unwind': '$foodgroups'}, foodgroup
    ]
    df = (meals.aggregate_pandas_all(pipeline,  schema = FoodGroupsSchema))
    df = df.rename(columns={'_id': 'Food Group', 'count': 'Count'})

    return(df)

def getAvgIntakeData1Month():
    #dateToday = date.today()
    dateToday = date.fromisoformat("2023-11-23")
    dateLastMonth = dateToday - timedelta(weeks=4)
    pipeline = [
        { '$match': {'date': { '$lte': dateToday.isoformat(), '$gte': dateLastMonth.isoformat()}}},
        avgintakegroup
    ]
    df = (intakes.aggregate_pandas_all(pipeline,  schema = AvgIntakeSchema))
    df = df.rename(columns={'_id':'date'})
    df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d").dt.date
    df = df.sort_values(by='date')

    return(df)

def getAvgIntakeData3Month():
    #dateToday = date.today()
    dateToday = date.fromisoformat("2023-11-23")
    dateLastMonth = dateToday - timedelta(weeks=4)
    pipeline = [
        { '$match': {'date': { '$lte': dateToday.isoformat(), '$gte': dateLastMonth.isoformat()}}},
        avgintakegroup
    ]
    df = (intakes.aggregate_pandas_all(pipeline,  schema = AvgIntakeSchema))
    df = df.rename(columns={'_id':'date'})
    df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d").dt.date
    df = df.sort_values(by='date')

    return(df)

def getAvgIntakeData6Month():
    #dateToday = date.today()
    dateToday = date.fromisoformat("2023-11-23")
    dateLastMonth = dateToday - timedelta(weeks=24)
    pipeline = [
        { '$match': {'date': { '$lte': dateToday.isoformat(), '$gte': dateLastMonth.isoformat()}}},
        avgintakegroup
    ]
    df = (intakes.aggregate_pandas_all(pipeline,  schema = AvgIntakeSchema))
    df = df.rename(columns={'_id':'date'})
    df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d").dt.date
    df = df.sort_values(by='date')

    return(df)

def getIntakeCountDaily():
    #dateToday = date.today()
    dateToday = date.fromisoformat("2023-11-23")
    pipeline = [
        { '$match': {'date': dateToday.isoformat()}},  
        intakecountproject
    ]

    return(intakes.aggregate_pandas_all(pipeline, schema = IntakeCountSchema))

def getIntakeCountWeekly():
    #dateToday = date.today()
    dateToday = date.fromisoformat("2023-11-23")
    dateLastWeek = dateToday - timedelta(days=7)
    pipeline = [
        { '$match': {'date': { '$lte': dateToday.isoformat(), '$gte': dateLastWeek.isoformat()}}},  
        intakecountproject
    ]

    return(intakes.aggregate_pandas_all(pipeline, schema = IntakeCountSchema))

def getIntakeCountMonthly():
    #dateToday = date.today()
    dateToday = date.fromisoformat("2023-11-23")
    dateLastMonth = dateToday - timedelta(days=28)
    pipeline = [
        { '$match': {'date': { '$lte': dateToday.isoformat(), '$gte': dateLastMonth.isoformat()}}},  
        intakecountproject
    ]

    return(intakes.aggregate_pandas_all(pipeline, schema = IntakeCountSchema))

def getMealStatsDaily():
    #dateToday = date.today().isoformat()
    dateToday = date.fromisoformat("2023-11-23")
    datetimeToday = datetime.fromisoformat(dateToday.isoformat())
    datetimeYesterday = datetimeToday - timedelta(days=1)
    pipeline = [
        { '$match': {'datetime': { '$lte': datetimeToday, '$gte': datetimeYesterday}}},    
        foodcountproject
    ]

    return(meals.aggregate_pandas_all(pipeline, schema = FoodCountSchema))

def getMealStatsWeekly():
    #dateToday = date.today().isoformat()
    dateToday = date.fromisoformat("2023-11-23")
    datetimeToday = datetime.fromisoformat(dateToday.isoformat())
    datetimeLastWeek = datetimeToday - timedelta(days=7)
    pipeline = [
        { '$match': {'datetime': { '$lte': datetimeToday, '$gte': datetimeLastWeek}}},    
        foodcountproject
    ]

    return(meals.aggregate_pandas_all(pipeline, schema = FoodCountSchema))

def getMealStatsMonthly():
    #dateToday = datetime.today()
    dateToday = date.fromisoformat("2023-11-23")
    datetimeToday = datetime.fromisoformat(dateToday.isoformat())
    datetimeLastMonth = datetimeToday - timedelta(weeks=10)
    pipeline = [
        { '$match': {'datetime': { '$lte': datetimeToday, '$gte': datetimeLastMonth}}},   
        foodcountproject
    ]

    return(meals.aggregate_pandas_all(pipeline, schema = FoodCountSchema))