from fastapi import APIRouter
from controller.charts_controller import getFoodGroupsDaily, getFoodGroupsWeekly, getFoodGroupsMonthly, getAvgIntake1Month, getAvgIntake3Month, getAvgIntake6Month, getIntakeCountDaily, getIntakeCountWeekly, getIntakeCountMonthly

router = APIRouter(
    prefix="/charts"
)

@router.get("/foodgroups/daily")
async def get_food_groups_daily():
    return getFoodGroupsDaily()

@router.get("/foodgroups/weekly")
async def get_food_groups_weekly():
    return getFoodGroupsWeekly()

@router.get("/foodgroups/monthly")
async def get_food_groups_monthly():
    return getFoodGroupsMonthly()

@router.get("/intakecharts/monthly")
async def get_monthly_avg_intake():
    return getAvgIntake1Month()

@router.get("/intakecharts/3month")
async def get_3month_avg_intake():
    return getAvgIntake3Month()

@router.get("/intakecharts/6monthly")
async def get_6month_avg_intake():
    return getAvgIntake6Month()

@router.get("/intakecount/daily")
async def get_intake_count_daily():
    return getIntakeCountDaily()

@router.get("/intakecount/weekly")
async def get_intake_count_weekly():
    return getIntakeCountWeekly()

@router.get("/intakecount/monthly")
async def get_intake_count_monthly():
    return getIntakeCountMonthly()