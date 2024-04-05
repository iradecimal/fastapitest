import plotly.express as px
import plotly.graph_objects as go
from pandas import DataFrame, Series
from bson.json_util import loads

def makeFoodGroupBar(df: DataFrame, x: str, y: str, orient: str, color: str, yaxis: str) -> go.Figure:
    fig = px.bar(df, x=x, y=y, orientation=orient, color=color)
    fig.update_layout(xaxis_title = "Date", yaxis_title = yaxis, xaxis={'categoryorder':'total descending'})

    return fig

def makeAvgIntakeBar(x: Series, y: Series, color: str, xaxis: str) -> go.Figure: 
    fig = go.Figure(go.Bar(x=x, y=y, marker_color=color))
    fig.update_layout(xaxis_title=xaxis, yaxis_title="Count")

    return fig

def makeHistogram(df: DataFrame, x: str, color: str, xaxis: str) -> go.Figure:
    fig = go.Figure(px.histogram(df, x=x, color_discrete_sequence=color, marginal='box'))
    fig.update_layout(xaxis_title = xaxis, yaxis_title = "Count", bargap=0.05)

    return fig

def makeAvgIntakeGraphs(df: DataFrame) -> list:
    figdailycal = makeAvgIntakeBar(df.date, df.dailycal, 'rgb(46, 184, 46)', "Daily Caloric Intake")

    figsleep = makeAvgIntakeBar(df.date, df.sleephrs, 'rgb(119, 51, 255)', "Average Hours of Sleep")

    figwater = makeAvgIntakeBar(df.date, df.waterglass, 'rgb(0, 172, 230)', "Average Water Intake in Glasses")

    figsteps = makeAvgIntakeBar(df.date, df.steps, 'rgb(51, 204, 51)', "Average Steps Taken Daily")

    data = [{
         "dailycalplot": loads(figdailycal.to_json()),
         "sleepplot": loads(figsleep.to_json()),
         "waterplot": loads(figwater.to_json()),
         "stepsplot": loads(figsteps.to_json()),
    }]
    return(data)

def makeIntakeHistograms(df: DataFrame) -> list:
    figdailycal = makeHistogram(df, "dailycal", ['rgb(46, 184, 46)'], "Caloric Intake")

    figsleep = makeHistogram(df, "sleephrs", ['rgb(119, 51, 255)'], "Hours of Sleep")

    figwater = makeHistogram(df, "waterglass", ['rgb(0, 172, 230)'], "Water Intake in Glasses")

    figsteps = makeHistogram(df, "steps", ['rgb(51, 204, 51)'], "Steps Taken Daily")

    data = [{
         "dailycalplot": loads(figdailycal.to_json()),
         "sleepplot": loads(figsleep.to_json()),
         "waterplot": loads(figwater.to_json()),
         "stepsplot": loads(figsteps.to_json()),
    }]
    return(data)

def makeFoodHistograms(df: DataFrame) -> list:
    figfat = makeHistogram(df, "fat", ['rgb(255, 153, 0)'], "Fat Intake")

    figcarbs = makeHistogram(df, "carbs", ['rgb(115, 230, 0)'], "Carb Intake")
    
    figproteins = makeHistogram(df, "proteins", ['rgb(179, 36, 0)'], "Protein Intake")

    figcal = makeHistogram(df, "cal", ['rgb(77, 136, 255)'], "Calories per Meal")
    
    figwaste = makeHistogram(df, "waste", ['rgb(102, 0, 51)'], "Waste")

    data = [{
        "fatplot": loads(figfat.to_json()),
        "carbsplot": loads(figcarbs.to_json()),
        "proteinsplot": loads(figproteins.to_json()),
        "calplot": loads(figcal.to_json()),
        "wasteplot": loads(figwaste.to_json())
    }]
    return(data)