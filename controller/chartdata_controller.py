from db import intakes, meals
from datetime import date, datetime, timedelta
import pandas as pd
from pymongoarrow.api import Schema

def getFoodGroupsDataDaily():
    #dateToday = datetime.today()
    dateToday = date.fromisoformat("2023-11-23")
    datetimeToday = datetime.fromisoformat(dateToday.isoformat())
    datetimeYesterday = datetimeToday - timedelta(days=1)
    pipeline = [
    { '$match': {'datetime': { '$lte': datetimeToday, '$gte': datetimeYesterday}}},  
    {'$unwind': '$foodgroups'}, 
    {'$group': {
            '_id': '$foodgroups', 
            'count': {'$sum': 1}
            }}]
    df = (meals.aggregate_pandas_all(pipeline,
    schema=Schema({'_id': str, 'count': int})))
    df = df.rename(columns={'_id': 'Food Group', 'count': 'Count'})

    return df

def getFoodGroupsDataWeekly():
    #dateToday = datetime.today()
    dateToday = date.fromisoformat("2023-11-23")
    datetimeToday = datetime.fromisoformat(dateToday.isoformat())
    datetimeLastWeek = datetimeToday - timedelta(days=7)
    pipeline = [
    { '$match': {'datetime': { '$lte': datetimeToday, '$gte': datetimeLastWeek}}},    
    {'$unwind': '$foodgroups'}, 
    {'$group': {
            '_id': '$foodgroups', 
            'count': {'$sum': 1}
            }}]
    df = (meals.aggregate_pandas_all(pipeline,
    schema=Schema({'_id': str, 'count': int})))
    df = df.rename(columns={'_id': 'Food Group', 'count': 'Count'})

    return df

def getFoodGroupsDataMonthly():
    #dateToday = datetime.today()
    dateToday = date.fromisoformat("2023-11-23")
    datetimeToday = datetime.fromisoformat(dateToday.isoformat())
    datetimeLastMonth = datetimeToday - timedelta(weeks=10)
    pipeline = [
    { '$match': {'datetime': { '$lte': datetimeToday, '$gte': datetimeLastMonth}}}, 
    {'$unwind': '$foodgroups'}, 
    {'$group': {
            '_id': '$foodgroups', 
            'count': {'$sum': 1}
            }}]
    df = (meals.aggregate_pandas_all(pipeline,
    schema=Schema({'_id': str, 'count': int})))
    df = df.rename(columns={'_id': 'Food Group', 'count': 'Count'})

    return(df)

def getAvgIntakeData1Month():
    #dateToday = date.today()
    dateToday = date.fromisoformat("2023-11-23")
    dateLastMonth = dateToday - timedelta(weeks=4)
    pipeline = [
        { '$match': {'date': { '$lte': dateToday.isoformat(), '$gte': dateLastMonth.isoformat()}}},
        {'$group': {
            '_id': '$date',
            'steps': {'$avg': '$steps'},
            'sleephrs': {'$avg': '$sleephrs'},
            'waterglass': {'$avg': '$waterglass'},
            'dailycal': {'$avg': '$dailycal'},
        }}]
    df = (intakes.aggregate_pandas_all(pipeline,
    schema=Schema({'_id': str, 'waterglass': float, 'sleephrs': float, 'dailycal': float, 'steps': float})
    ))
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
        {'$group': {
            '_id': '$date',
            'steps': {'$avg': '$steps'},
            'sleephrs': {'$avg': '$sleephrs'},
            'waterglass': {'$avg': '$waterglass'},
            'dailycal': {'$avg': '$dailycal'},
        }}]
    df = (intakes.aggregate_pandas_all(pipeline,
    schema=Schema({'_id': str, 'waterglass': float, 'sleephrs': float, 'dailycal': float, 'steps': float})
    ))
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
        {'$group': {
            '_id': '$date',
            'steps': {'$avg': '$steps'},
            'sleephrs': {'$avg': '$sleephrs'},
            'waterglass': {'$avg': '$waterglass'},
            'dailycal': {'$avg': '$dailycal'},
        }}]
    df = (intakes.aggregate_pandas_all(pipeline,
    schema=Schema({'_id': str, 'waterglass': float, 'sleephrs': float, 'dailycal': float, 'steps': float})
    ))
    df = df.rename(columns={'_id':'date'})
    df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d").dt.date
    df = df.sort_values(by='date')

    return(df)

def getAvgIntakeData1Year():
    #dateToday = date.today()
    dateToday = date.fromisoformat("2023-11-23")
    dateLastMonth = dateToday - timedelta(years=1)
    pipeline = [
        { '$match': {'date': { '$lte': dateToday.isoformat(), '$gte': dateLastMonth.isoformat()}}},
        {'$group': {
            '_id': '$date',
            'steps': {'$avg': '$steps'},
            'sleephrs': {'$avg': '$sleephrs'},
            'waterglass': {'$avg': '$waterglass'},
            'dailycal': {'$avg': '$dailycal'},
        }}]
    df = (intakes.aggregate_pandas_all(pipeline,
    schema=Schema({'_id': str, 'waterglass': float, 'sleephrs': float, 'dailycal': float, 'steps': float})
    ))
    df = df.rename(columns={'_id':'date'})
    df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d").dt.date
    df = df.sort_values(by='date')

    return(df)

def getIntakeCountDaily():
    #dateToday = date.today()
    dateToday = date.fromisoformat("2023-11-23")
    
    pipeline = [
        { '$match': {'date': dateToday.isoformat()}},  
        {'$project': {
            "waterglass": "$waterglass",
            "sleephrs": "$sleephrs",
            "dailycal": "$dailycal",
            "steps": "$steps",
            }}]

    return((intakes.aggregate_pandas_all(pipeline,
    schema=Schema({'waterglass': int, 'sleephrs': float, 'dailycal': int, 'steps': int}))))

def getIntakeCountWeekly():
    #dateToday = date.today()
    dateToday = date.fromisoformat("2023-11-23")
    dateLastWeek = dateToday - timedelta(days=7)
    
    pipeline = [
        { '$match': {'date': { '$lte': dateToday.isoformat(), '$gte': dateLastWeek.isoformat()}}},  
        {'$project': {
            "waterglass": "$waterglass",
            "sleephrs": "$sleephrs",
            "dailycal": "$dailycal",
            "steps": "$steps",
            }}]

    return((intakes.aggregate_pandas_all(pipeline,
    schema=Schema({'waterglass': int, 'sleephrs': float, 'dailycal': int, 'steps': int}))))

def getIntakeCountMonthly():
    #dateToday = date.today()
    dateToday = date.fromisoformat("2023-11-23")
    dateLastMonth = dateToday - timedelta(days=28)
    pipeline = [
        { '$match': {'date': { '$lte': dateToday.isoformat(), '$gte': dateLastMonth.isoformat()}}},  
        {'$project': {
            "waterglass": "$waterglass",
            "sleephrs": "$sleephrs",
            "dailycal": "$dailycal",
            "steps": "$steps",
            }}]

    return((intakes.aggregate_pandas_all(pipeline,
    schema=Schema({'waterglass': int, 'sleephrs': float, 'dailycal': int, 'steps': int}))))