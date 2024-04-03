from fastapi import APIRouter
from controller.intake_controller import getAvgIntakeWeek, getAvgIntake1Month, getAvgIntake3Month, getIntakePlotDaily, getIntakePlotWeekly, getIntakePlotMonthly

router = APIRouter(
    prefix = "/intakes"
)

@router.get("/avg/weekly")
async def get_weekly_avg_intake():
    return getAvgIntakeWeek()

@router.get("/avg/monthly")
async def get_monthly_avg_intake():
    return getAvgIntake1Month()

@router.get("/avg/3monthly")
async def get_3month_avg_intake():
    return getAvgIntake3Month()

@router.get("/count/daily")
async def get_intake_count_daily():
    return getIntakePlotDaily()

@router.get("/count/weekly")
async def get_intake_count_weekly():
    return getIntakePlotWeekly()

@router.get("/count/monthly")
async def get_intake_count_monthly():
    return getIntakePlotMonthly()
