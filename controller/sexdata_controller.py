from db import intakes
from datetime import date, timedelta
from pymongoarrow.api import Schema
import pandas as pd

SexIntakeCountSchema =Schema({'sex': str, 'waterglass': float, 'sleephrs': float, 'dailycal': float, 'steps': float})

SexAvgIntakeSchema = Schema({'date': str, 'sex': str, 'waterglass': float, 'sleephrs': float, 'dailycal': float, 'steps': float})

lookupUser = { '$lookup': {
        'from': "users",
        'localField': "uid",
        'foreignField': "_id",
        'as': "user_data",
}}

projectData = {'$project': {
    "sex": '$user_data.sex',
    "waterglass": "$waterglass",
    "sleephrs": "$sleephrs",
    "dailycal": "$dailycal",
    "steps": "$steps",
}}

groupAvg = { '$group': {
    "_id": {'date': '$date', 'sex': '$user_data.sex'},
    'steps': {'$avg': '$steps'},
    'sleephrs': {'$avg': '$sleephrs'},
    'waterglass': {'$avg': '$waterglass'},
    'dailycal': {'$avg': '$dailycal'}
}}

projectAvg = { '$project': {
    'date': '$_id.date', 
    'sex': '$_id.sex',
    'steps': '$steps',
    'sleephrs': '$sleephrs',
    'waterglass': '$waterglass',
    'dailycal': '$dailycal',
}}




def getIntakeCountSexWeekly():
    #dateToday = date.today()
    dateToday = date.fromisoformat("2023-11-23")
    dateLastWeek = dateToday - timedelta(days=7)
    pipeline = [
        { '$match': {'date': { '$lte': dateToday.isoformat(), '$gte': dateLastWeek.isoformat()}}}, 
        lookupUser, 
        { '$unwind': '$user_data'},
        projectData
    ]

    df = (intakes.aggregate_pandas_all(pipeline, schema = SexIntakeCountSchema))
    
    return df

def getIntakeCountSexMonthly():
    #dateToday = date.today()
    dateToday = date.fromisoformat("2023-11-23")
    dateLastMonth = dateToday - timedelta(weeks=4)
    pipeline = [
        { '$match': {'date': { '$lte': dateToday.isoformat(), '$gte': dateLastMonth.isoformat()}}}, 
        lookupUser, 
        { '$unwind': '$user_data'}, 
        projectData
    ]

    df = (intakes.aggregate_pandas_all(pipeline, schema = SexIntakeCountSchema))
    
    return df

def getIntakeAvgSexWeekly():
    #dateToday = date.today()
    dateToday = date.fromisoformat("2023-11-23")
    dateLastWeek = dateToday - timedelta(days=7)
    pipeline = [
        { '$match': {'date': { '$lte': dateToday.isoformat(), '$gte': dateLastWeek.isoformat()}}}, 
        lookupUser, { '$unwind': '$user_data'},
        { '$group': {
            "_id": {'date': '$date', 'sex': '$user_data.sex'},
            'steps': {'$avg': '$steps'},
            'sleephrs': {'$avg': '$sleephrs'},
            'waterglass': {'$avg': '$waterglass'},
            'dailycal': {'$avg': '$dailycal'}
        }}, projectAvg
    ]

    df = intakes.aggregate_pandas_all(pipeline, schema = SexAvgIntakeSchema)
    df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d").dt.date
    df = df.sort_values(by='date')
    
    return df

def getIntakeAvgSexMonthly():
    #dateToday = date.today()
    dateToday = date.fromisoformat("2023-11-23")
    dateLastMonth = dateToday - timedelta(weeks=4)
    pipeline = [
        { '$match': {'date': { '$lte': dateToday.isoformat(), '$gte': dateLastMonth.isoformat()}}}, 
        lookupUser, { '$unwind': '$user_data'},
        { '$group': {
            "_id": {'date': '$date', 'sex': '$user_data.sex'},
            'steps': {'$avg': '$steps'},
            'sleephrs': {'$avg': '$sleephrs'},
            'waterglass': {'$avg': '$waterglass'},
            'dailycal': {'$avg': '$dailycal'}
        }}, projectAvg
    ]

    df = intakes.aggregate_pandas_all(pipeline, schema = SexAvgIntakeSchema)
    df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d").dt.date
    df = df.sort_values(by='date')
    
    return df