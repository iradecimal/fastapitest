import plotly.express as px
import plotly.graph_objects as go
from pandas import DataFrame, Series
from bson.json_util import loads

genders={"M": "rgb(102, 153, 255)","F": "rgb(255, 102, 153)"}

def makeSexLine(df: DataFrame, y:str, title:str, yaxis: str)  -> go.Figure:
    fig = px.line(df, x="date", y=y, color="sex", color_discrete_map=genders, title=title, markers = True)
    fig.update_layout(xaxis_title = "Date", yaxis_title= yaxis)
    return fig

def makeSexHistogram(df: DataFrame, x: str, title:str, nbins:int, xaxis: str) -> go.Figure:
    fig = px.histogram(df, x=x, color="sex", title=title, marginal = 'box', nbins=nbins, color_discrete_map=genders)
    fig.update_layout(xaxis_title = xaxis, yaxis_title = "Count")
    return fig

def makeIntakeSexHistograms(df: DataFrame) -> list:
    figdailycal = makeSexHistogram(df, "dailycal", "Daily Caloric Intake Count", 12, "Caloric Intake")

    figsleep = makeSexHistogram(df, "sleephrs", "Daily Sleep Hour Count", 8, "Hours of Sleep")

    figwater = makeSexHistogram(df, "waterglass", "Daily Water Glass Intake Count", 6,"Water Intake in Glasses")

    figsteps = makeSexHistogram(df, "steps", "Daily Steps Count", 6, "Steps Taken Daily")

    data = [{
         "dailycalplot": loads(figdailycal.to_json()),
         "sleepplot": loads(figsleep.to_json()),
         "waterplot": loads(figwater.to_json()),
         "stepsplot": loads(figsteps.to_json()),
    }]
    return(data)

def makeAvgIntakeSexGraphs(df: DataFrame) -> list:
    figdailycal = makeSexLine(df, "dailycal", "Daily Caloric Intake", "Calories")

    figsleep = makeSexLine(df, "sleephrs", "Average Hours of Sleep", "Sleep Hours")

    figwater = makeSexLine(df, "waterglass", "Average Water Intake in Glasses", "Water Glasses")

    figsteps = makeSexLine(df, "steps", "Average Steps Taken Daily", "Steps")

    data = [{
         "dailycalplot": loads(figdailycal.to_json()),
         "sleepplot": loads(figsleep.to_json()),
         "waterplot": loads(figwater.to_json()),
         "stepsplot": loads(figsteps.to_json()),
    }]
    return(data)