from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from routes import avgstats, charts, trends, find, sex



app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"] 
)

app.include_router(avgstats.router, tags=["stats"])
app.include_router(charts.router, tags=["charts"])
app.include_router(find.router, tags=["find"])
app.include_router(trends.router, tags=["trends"])
app.include_router(sex.router, tags=["sex"])
#trends
#meals
#intakes