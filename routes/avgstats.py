from fastapi import APIRouter
from controller.avgstats_controller import getIntakeStatsDaily, getIntakeStatsWeekly, getIntakeStatsMonthly, getMealStatsDaily, getMealStatsWeekly, getMealStatsMonthly

router = APIRouter(
    prefix="/stats"
)

@router.get("/daily/intake")
async def get_daily_intake_stats():
    return getIntakeStatsDaily()

@router.get("/weekly/intake")
async def get_weekly_intake_stats():
    return getIntakeStatsWeekly()

@router.get("/monthly/intake")
async def get_monthly_intake_stats():
    return getIntakeStatsMonthly()

@router.get("/daily/meals")
async def get_daily_meal_stats():
    return getMealStatsDaily()

@router.get("/weekly/meals")
async def get_weekly_intake_stats():
    return getMealStatsWeekly()

@router.get("/monthly/meals")
async def get_monthly_meal_stats():
    return getMealStatsMonthly()

@router.get("/activity")
async def get_user_activity_stats():
    return 1