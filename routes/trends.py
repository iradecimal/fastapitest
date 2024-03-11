from fastapi import APIRouter
from controller.trend_controller import getIntakeTrends1Month, getIntakeTrends3Month

router = APIRouter(
    prefix="/trends"
)

@router.get("/intake/monthly")
async def get_1month_intake_trends():
    return getIntakeTrends1Month() 

@router.get("/intake/3monthly")
async def get_3month_intake_trends():
    return getIntakeTrends3Month() 