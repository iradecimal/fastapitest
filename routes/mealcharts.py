from fastapi import APIRouter, Query
from typing import Annotated
from controller.meal_controller import getFoodGroupsDaily, getFoodGroupsWeekly, getFoodGroupsMonthly, getMealCountDaily, getMealCountWeekly, getMealCountMonthly, getMealCountDailySex, getMealCountWeeklySex, getMealCountMonthlySex

router = APIRouter(
    prefix = "/meals"
)

@router.get("/foodgroups/daily")
async def get_food_groups_daily(sex: Annotated[str | None, Query(max_length=1)] = None):
    if sex:
        if sex == "m":
            return getMealCountDailySex('F')
        elif sex == "f":
            return getMealCountDailySex('M')
    else:
        return getFoodGroupsDaily()

@router.get("/foodgroups/weekly")
async def get_food_groups_weekly(sex: Annotated[str | None, Query(max_length=1)] = None):
    if sex:
        if sex == "m":
            return getMealCountDailySex('F')
        elif sex == "f":
            return getMealCountDailySex('M')
    else:
        return getFoodGroupsWeekly()

@router.get("/foodgroups/monthly")
async def get_food_groups_monthly(sex: Annotated[str | None, Query(max_length=1)] = None):
    if sex:
        if sex == "m":
            return getMealCountDailySex('F')
        elif sex == "f":
            return getMealCountDailySex('M')
    else:
        return getFoodGroupsMonthly()

@router.get("/count/daily")
async def get_meal_count_daily(sex: Annotated[str | None, Query(max_length=1)] = None):
    if sex:
        if sex == "m":
            return getMealCountDailySex('F')
        elif sex == "f":
            return getMealCountDailySex('M')
    else:
        return getMealCountDaily()

@router.get("/count/weekly")
async def get_meal_count_weekly(sex: Annotated[str | None, Query(max_length=1)] = None):
    if sex:
        if sex == "m":
            return getMealCountWeeklySex('F')
        elif sex == "f":
            return getMealCountWeeklySex('M')
    else:
        return getMealCountWeekly()

@router.get("/count/monthly")
async def get_meal_count_monthly(sex: Annotated[str | None, Query(max_length=1)] = None):
    if sex:
        if sex == "m":
            return getMealCountMonthlySex('F')
        elif sex == "f":
            return getMealCountMonthly('M')
    else:
        return getMealCountDaily()

@router.get("/avg/weekly")
async def get_weekly_avg_meal():
    return getMealAvgWeekly()

@router.get("/avg/monthly")
async def get_monthly_avg_meal():
    return getMealAvgMonthly()