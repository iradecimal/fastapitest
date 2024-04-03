from fastapi import APIRouter
from controller.meal_controller import getFoodGroupsDaily, getFoodGroupsWeekly, getFoodGroupsMonthly, getMealCountDaily, getMealCountWeekly, getMealCountMonthly

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

@router.get("/mealcount/daily")
async def get_meal_count_daily():
    return getMealCountDaily()

@router.get("/mealcount/weekly")
async def get_meal_count_weekly():
    return getMealCountWeekly()

@router.get("/mealcount/monthly")
async def get_meal_count_monthly():
    return getMealCountMonthly()
