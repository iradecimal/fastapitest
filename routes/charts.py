from fastapi import APIRouter
from controller.charts_controller import getFoodGroupsDaily, getFoodGroupsWeekly, getFoodGroupsMonthly, getAvgIntakeWeek, getAvgIntake1Month, getAvgIntake3Month, getIntakePlotDaily, getIntakePlotWeekly, getIntakePlotMonthly, getMealCountDaily, getMealCountWeekly, getMealCountMonthly

router = APIRouter(
    prefix = "/charts"
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

@router.get("/intakecharts/weekly")
async def get_weekly_avg_intake():
    return getAvgIntakeWeek()

@router.get("/intakecharts/monthly")
async def get_monthly_avg_intake():
    return getAvgIntake1Month()

@router.get("/intakecharts/3monthly")
async def get_3month_avg_intake():
    return getAvgIntake3Month()

@router.get("/intakecount/daily")
async def get_intake_count_daily():
    return getIntakePlotDaily()

@router.get("/intakecount/weekly")
async def get_intake_count_weekly():
    return getIntakePlotWeekly()

@router.get("/intakecount/monthly")
async def get_intake_count_monthly():
    return getIntakePlotMonthly()

@router.get("/mealcount/daily")
async def get_meal_count_daily():
    return getMealCountDaily()

@router.get("/mealcount/weekly")
async def get_meal_count_weekly():
    return getMealCountWeekly()

@router.get("/mealcount/monthly")
async def get_meal_count_monthly():
    return getMealCountMonthly()
