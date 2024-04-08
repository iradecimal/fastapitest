from fastapi import APIRouter
from controller.meal_controller import getFoodGroupsDaily, getFoodGroupsWeekly, getFoodGroupsMonthly, getMealCountDaily, getMealCountWeekly, getMealCountMonthly, getMealAvgWeekly, getMealAvgMonthly

router = APIRouter(
    prefix = "/meals"
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

@router.get("/count/daily")
async def get_meal_count_daily():
    return getMealCountDaily()

@router.get("/count/weekly")
async def get_meal_count_weekly():
    return getMealCountWeekly()

@router.get("/count/monthly")
async def get_meal_count_monthly():
    return getMealCountMonthly()

@router.get("/avg/weekly")
async def get_weekly_avg_meal():
    return getMealAvgWeekly()

@router.get("/avg/monthly")
async def get_monthly_avg_meal():
    return getMealAvgMonthly()