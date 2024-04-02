from db import intakes, meals, users
from datetime import date, datetime, timedelta
from bson.json_util import loads, dumps
from pymongoarrow.api import Schema

AvgIntakeSchema = Schema({'hale': float, 'phd': float, 'waterglass': float, 'sleephrs': float, 'dailycal': float, 'steps': float})
AvgFoodSchema = Schema({'fat': float, 'carbs': float, 'protein': float, 'cal': float, 'waste': float})

def getIntakeStatsDaily():
    #dateToday = date.today().isoformat()
    dateToday = date.fromisoformat("2023-11-23")
    pipeline = [
    { '$match': {'date': dateToday.isoformat()}},    
    { '$group': {
            "_id": None,
            "hale": {'$avg': '$hale'},
            'phd': {'$avg': '$phd'},
            'steps': {'$avg': '$steps'},
            'sleephrs': {'$avg': '$sleephrs'},
            'waterglass': {'$avg': '$waterglass'},
            'dailycal': {'$avg': '$dailycal'},
        }}]
    find = (intakes.aggregate(pipeline)) 
    return(loads(dumps(find)))

def getIntakeStatsWeekly():
    #dateToday = date.today()
    dateToday = date.fromisoformat("2023-11-23")
    dateLastWeek = dateToday - timedelta(days=7) 
    pipeline = [
    { '$match': {'date': { '$lte': dateToday.isoformat(), '$gte': dateLastWeek.isoformat()}}},    
    { '$group': {
            "_id": None,
            "hale": {'$avg': '$hale'},
            'phd': {'$avg': '$phd'},
            'steps': {'$avg': '$steps'},
            'sleephrs': {'$avg': '$sleephrs'},
            'waterglass': {'$avg': '$waterglass'},
            'dailycal': {'$avg': '$dailycal'},
        }}]
    find = (intakes.aggregate(pipeline)) 
    return(loads(dumps(find)))


def getIntakeStatsMonthly(): 
    #dateToday = date.today()
    dateToday = date.fromisoformat("2023-11-23")
    dateLastMonth = dateToday - timedelta(weeks=4)
    pipeline = [
    { '$match': {'date': { '$lte': dateToday.isoformat(), '$gte': dateLastMonth.isoformat()}}},    
    { '$group': {
            "_id": None,
            "hale": {'$avg': '$hale'},
            'phd': {'$avg': '$phd'},
            'steps': {'$avg': '$steps'},
            'sleephrs': {'$avg': '$sleephrs'},
            'waterglass': {'$avg': '$waterglass'},
            'dailycal': {'$avg': '$dailycal'},
        }}]
    find = (intakes.aggregate(pipeline)) 
    return(loads(dumps(find)))

def getMealStatsDaily():
    #dateToday = date.today().isoformat()
    dateToday = date.fromisoformat("2023-11-23")
    datetimeToday = datetime.fromisoformat(dateToday.isoformat())
    datetimeYesterday = datetimeToday - timedelta(days=1)
    pipeline = [
    { '$match': {'datetime': { '$lte': datetimeToday, '$gte': datetimeYesterday}}},    
    { '$group': {
            "_id": None,
            'fat': {'$avg': '$fat'},
            'carbs': {'$avg': '$carbs'},
            'proteins': {'$avg': '$proteins'},
            'cal': {'$avg': '$cal'},
            'waste': {'$avg': '$waste'},
        }}]
    find = (meals.aggregate(pipeline)) 
    return(loads(dumps(find)))


def getMealStatsWeekly():
    #dateToday = date.today()
    dateToday = date.fromisoformat("2023-11-23")
    datetimeToday = datetime.fromisoformat(dateToday.isoformat())
    datetimeLastWeek = datetimeToday - timedelta(days=7)
    pipeline = [
    { '$match': {'datetime': { '$lte': datetimeToday, '$gte': datetimeLastWeek}}},
    { '$group': {
            "_id": None,
            'fat': {'$avg': '$fat'},
            'carbs': {'$avg': '$carbs'},
            'proteins': {'$avg': '$proteins'},
            'cal': {'$avg': '$cal'},
            'waste': {'$avg': '$waste'},
        }}]
    find = (meals.aggregate(pipeline)) 
    return(loads(dumps(find)))

def getMealStatsMonthly():
    #dateToday = date.today()
    dateToday = date.fromisoformat("2023-11-23")
    datetimeToday = datetime.fromisoformat(dateToday.isoformat())
    datetimeLastMonth = datetimeToday - timedelta(weeks=4)
    pipeline = [
    { '$match': {'datetime': { '$lte': datetimeToday, '$gte': datetimeLastMonth}}},      
    { '$group': {
            "_id": None,
            'fat': {'$avg': '$fat'},
            'carbs': {'$avg': '$carbs'},
            'proteins': {'$avg': '$proteins'},
            'cal': {'$avg': '$cal'},
            'waste': {'$avg': '$waste'},
        }}]
    find = (meals.aggregate(pipeline)) 
    return(loads(dumps(find)))