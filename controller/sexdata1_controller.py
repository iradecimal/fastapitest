from db import intakes
from datetime import date, timedelta
from pymongoarrow.api import Schema
import pandas as pd

SexIntakeCountSchema =Schema({'sex': str, 'waterglass': float, 'sleephrs': float, 'dailycal': float, 'steps': float})

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

def getDateInterval(interval: str):
    #dateToday = datetime.today()
    dateToday = date.fromisoformat("2023-11-23") #testing purposes
    dateBefore = ''
    if interval == "daily":
        dateBefore = dateToday - timedelta(days=1)
    elif interval == "weekly":
        dateBefore = dateToday - timedelta(weeks=1)
    elif interval == "monthly":
        dateBefore = dateToday - timedelta(weeks=4)
    elif interval == "3month":
        dateBefore = dateToday - timedelta(weeks=12)
    else:
        raise ValueError("Wrong interval was sent. Please check for capitalization/spelling errors.")
    dateInterval = { '$match': {'date': { '$lte': dateToday.isoformat(), '$gte': dateBefore.isoformat()}}}
    return dateInterval

def getIntakeCountSex(sex: str, interval: str):
    if (sex != 'M' and sex != 'F'):
        raise ValueError("Wrong sex was sent. Please check for capitalization/spelling errors.")
    pipeline = [
        getDateInterval(interval),
        lookupUser, 
        { '$unwind': '$user_data'},
        { '$match': { 'user_data.sex' : sex}},
        projectData
    ]

    df = (intakes.aggregate_pandas_all(pipeline, schema = SexIntakeCountSchema))
    
    return df

    