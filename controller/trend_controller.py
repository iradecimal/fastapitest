from .chartdata_controller import getAvgIntakeData1Month, getAvgIntakeData3Month
from .trendmaker_controller import makeIntakePredictions

#one month intake trends
def getIntakeTrends1Month():
    df = getAvgIntakeData1Month()
    return(makeIntakePredictions(df, 5))

def getIntakeTrends3Month():
    df = getAvgIntakeData3Month()
    return(makeIntakePredictions(df, 15))

    
#three month intake trends

#one month meal trends

#three month meal trends
