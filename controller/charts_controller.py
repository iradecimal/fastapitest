from datetime import date, datetime, timedelta
from bson.json_util import loads, dumps
import plotly.express as px
import plotly.graph_objects as go
from .chartdata_controller import getFoodGroupsDataDaily, getFoodGroupsDataWeekly, getFoodGroupsDataMonthly, getAvgIntakeData1Month, getAvgIntakeData3Month, getAvgIntakeData6Month, getAvgIntakeData1Year

def getFoodGroupsDaily():
    df = getFoodGroupsDataDaily()

    fig = px.bar(df, y='Food Group', x='Count', orientation="h", color="Food Group")
    fig.update_layout(xaxis_title = "Food Groups", yaxis_title = "Count")
    #fig.show()
    return(loads((fig.to_json())))

def getFoodGroupsWeekly():
    df = getFoodGroupsDataWeekly()

    fig = px.bar(df, y='Food Group', x='Count', orientation="h", color="Food Group")
    fig.update_layout(xaxis_title = "Food Groups", yaxis_title = "Count", xaxis={'categoryorder':'total descending'})
    #fig.show()
    return(loads((fig.to_json())))

def getFoodGroupsMonthly():
    df = getFoodGroupsDataMonthly()

    fig = px.bar(df, y='Food Group', x='Count', orientation="h", color="Food Group")
    fig.update_layout(xaxis_title = "Food Groups", yaxis_title = "Count")
    #fig.show()
    return(loads((fig.to_json())))

def getAvgIntake1Month():
    df = getAvgIntakeData1Month()

    figdailycal = go.Figure(go.Bar( x=df.date, y= df.dailycal, marker_color='rgb(46, 184, 46)'))
    figdailycal.update_layout(title="Average Daily Caloric Intake Last Month", xaxis_title = "date", yaxis_title = "Daily Caloric Intake")
    figdailycal.show()

    figsleep = go.Figure(go.Bar( x=df.date, y= df.sleephrs, marker_color='rgb(119, 51, 255)'))
    figsleep.update_layout(title="Average Sleep Duration Last Month", xaxis_title = "Date", yaxis_title = "Average Hours of Sleep")
    figsleep.show()

    figwater = go.Figure(go.Bar( x=df.date, y= df.waterglass, marker_color='rgb(0, 172, 230)'))
    figwater.update_layout(title="Average Water Intake Last Month", xaxis_title = "Date", yaxis_title = "Average Water Intake in Glasses")
    figwater.show()

    figsteps = go.Figure(go.Bar( x=df.date, y= df.steps, marker_color='rgb(51, 204, 51)'))
    figsteps.update_layout(title="Average Steps Taken Last Month", xaxis_title = "Date", yaxis_title = "Average Steps Taken Daily")
    figsteps.show()

    data = [{
        "dailycalplot": loads(figdailycal.to_json()),
        "sleepplot": loads(figsleep.to_json()),
        "waterplot": loads(figwater.to_json()),
        "stepsplot": loads(figsteps.to_json()),
    }]

    return(data)

def getAvgIntake1Month():
    df = getAvgIntakeData1Month()

    figdailycal = go.Figure(go.Bar( x=df.date, y= df.dailycal, marker_color='rgb(46, 184, 46)'))
    figdailycal.update_layout(title="Average Daily Caloric Intake Last Month", xaxis_title = "date", yaxis_title = "Daily Caloric Intake")

    figsleep = go.Figure(go.Bar( x=df.date, y= df.sleephrs, marker_color='rgb(119, 51, 255)'))
    figsleep.update_layout(title="Average Sleep Duration Last Month", xaxis_title = "Date", yaxis_title = "Average Hours of Sleep")

    figwater = go.Figure(go.Bar( x=df.date, y= df.waterglass, marker_color='rgb(0, 172, 230)'))
    figwater.update_layout(title="Average Water Intake Last Month", xaxis_title = "Date", yaxis_title = "Average Water Intake in Glasses")

    figsteps = go.Figure(go.Bar( x=df.date, y= df.steps, marker_color='rgb(51, 204, 51)'))
    figsteps.update_layout(title="Average Steps Taken Last Month", xaxis_title = "Date", yaxis_title = "Average Steps Taken Daily")

    data = [{
        "dailycalplot": loads(figdailycal.to_json()),
        "sleepplot": loads(figsleep.to_json()),
        "waterplot": loads(figwater.to_json()),
        "stepsplot": loads(figsteps.to_json()),
    }]

    return(data)

def getAvgIntake3Month():
    df = getAvgIntakeData3Month()

    figdailycal = go.Figure(go.Bar( x=df.date, y= df.dailycal, marker_color='rgb(46, 184, 46)'))
    figdailycal.update_layout(title="Average Daily Caloric Intake Last Month", xaxis_title = "date", yaxis_title = "Daily Caloric Intake")

    figsleep = go.Figure(go.Bar( x=df.date, y= df.sleephrs, marker_color='rgb(119, 51, 255)'))
    figsleep.update_layout(title="Average Sleep Duration Last Month", xaxis_title = "Date", yaxis_title = "Average Hours of Sleep")

    figwater = go.Figure(go.Bar( x=df.date, y= df.waterglass, marker_color='rgb(0, 172, 230)'))
    figwater.update_layout(title="Average Water Intake Last Month", xaxis_title = "Date", yaxis_title = "Average Water Intake in Glasses")

    figsteps = go.Figure(go.Bar( x=df.date, y= df.steps, marker_color='rgb(51, 204, 51)'))
    figsteps.update_layout(title="Average Steps Taken Last Month", xaxis_title = "Date", yaxis_title = "Average Steps Taken Daily")

    data = [{
        "dailycalplot": loads(figdailycal.to_json()),
        "sleepplot": loads(figsleep.to_json()),
        "waterplot": loads(figwater.to_json()),
        "stepsplot": loads(figsteps.to_json()),
    }]

    return(data)

def getAvgIntake6Month():
    df = getAvgIntakeData6Month()

    figdailycal = go.Figure(go.Bar( x=df.date, y= df.dailycal, marker_color='rgb(46, 184, 46)'))
    figdailycal.update_layout(title="Average Daily Caloric Intake Last Month", xaxis_title = "date", yaxis_title = "Daily Caloric Intake")

    figsleep = go.Figure(go.Bar( x=df.date, y= df.sleephrs, marker_color='rgb(119, 51, 255)'))
    figsleep.update_layout(title="Average Sleep Duration Last Month", xaxis_title = "Date", yaxis_title = "Average Hours of Sleep")

    figwater = go.Figure(go.Bar( x=df.date, y= df.waterglass, marker_color='rgb(0, 172, 230)'))
    figwater.update_layout(title="Average Water Intake Last Month", xaxis_title = "Date", yaxis_title = "Average Water Intake in Glasses")

    figsteps = go.Figure(go.Bar( x=df.date, y= df.steps, marker_color='rgb(51, 204, 51)'))
    figsteps.update_layout(title="Average Steps Taken Last Month", xaxis_title = "Date", yaxis_title = "Average Steps Taken Daily")

    data = [{
        "dailycalplot": loads(figdailycal.to_json()),
        "sleepplot": loads(figsleep.to_json()),
        "waterplot": loads(figwater.to_json()),
        "stepsplot": loads(figsteps.to_json()),
    }]

    return(data)

def getAvgIntake1Year():
    df = getAvgIntakeData1Year()

    figdailycal = go.Figure(go.Bar( x=df.date, y= df.dailycal, marker_color='rgb(46, 184, 46)'))
    figdailycal.update_layout(title="Average Daily Caloric Intake Last Month", xaxis_title = "date", yaxis_title = "Daily Caloric Intake")

    figsleep = go.Figure(go.Bar( x=df.date, y= df.sleephrs, marker_color='rgb(119, 51, 255)'))
    figsleep.update_layout(title="Average Sleep Duration Last Month", xaxis_title = "Date", yaxis_title = "Average Hours of Sleep")

    figwater = go.Figure(go.Bar( x=df.date, y= df.waterglass, marker_color='rgb(0, 172, 230)'))
    figwater.update_layout(title="Average Water Intake Last Month", xaxis_title = "Date", yaxis_title = "Average Water Intake in Glasses")

    figsteps = go.Figure(go.Bar( x=df.date, y= df.steps, marker_color='rgb(51, 204, 51)'))
    figsteps.update_layout(title="Average Steps Taken Last Month", xaxis_title = "Date", yaxis_title = "Average Steps Taken Daily")

    data = [{
        "dailycalplot": loads(figdailycal.to_json()),
        "sleepplot": loads(figsleep.to_json()),
        "waterplot": loads(figwater.to_json()),
        "stepsplot": loads(figsteps.to_json()),
    }]

    return(data)