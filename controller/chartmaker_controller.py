import plotly.express as px
import plotly.graph_objects as go
from pandas import DataFrame, Series
from bson.json_util import loads

def makeFoodGroupBar(df: DataFrame, x: str, y: str, orient: str, color: str, xaxis: str, yaxis: str) -> go.Figure:
    fig = px.bar(df, x=x, y=y, orientation=orient, color=color)
    fig.update_layout(xaxis_title = xaxis, yaxis_title = yaxis, xaxis={'categoryorder':'total descending'})

    return fig

def makeAvgIntakeBar(x: Series, y: Series, color: str, xaxis: str, yaxis: str) -> go.Figure: 
    fig = go.Figure(go.Bar(x=x, y=y, marker_color=color))
    fig.update_layout(xaxis_title=xaxis, yaxis_title=yaxis)

    return fig

def makeAvgIntakeGraphs(df: DataFrame) -> list:
    figdailycal = makeAvgIntakeBar(df.date, df.dailycal, 'rgb(46, 184, 46)', "Date", "Daily Caloric Intake")

    figsleep = makeAvgIntakeBar(df.date, df.sleephrs, 'rgb(119, 51, 255)', "Date", "Average Hours of Sleep")

    figwater = makeAvgIntakeBar(df.date, df.waterglass, 'rgb(0, 172, 230)', "Date", "Average Water Intake in Glasses")

    figsteps = makeAvgIntakeBar(df.date, df.steps, 'rgb(51, 204, 51)', "Date", "Average Steps Taken Daily")

    data = [{
         "dailycalplot": loads(figdailycal.to_json()),
         "sleepplot": loads(figsleep.to_json()),
         "waterplot": loads(figwater.to_json()),
         "stepsplot": loads(figsteps.to_json()),
    }]
    return(data)

def makeHistograms(x: Series, color: str, xaxis: str) -> go.Figure:
    fig = go.Figure(go.Histogram(x=x, marker_color=color))
    fig.update_layout(xaxis_title=xaxis)