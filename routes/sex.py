from fastapi import APIRouter
from controller.sex_controller import getSexIntakeCountWeekly, getSexIntakeCountMonthly, getSexAvgIntakeWeekly, getSexAvgIntakeMonthly

router = APIRouter(
    prefix = "/sex"
)

@router.get("/counts/weekly")
async def get_intake_count_sex_weekly():
    return getSexIntakeCountWeekly()

@router.get("/counts/monthly")
async def get_intake_count_sex_monthly():
    return getSexIntakeCountMonthly()

@router.get("/average/weekly")
async def get_intake_average_sex_weekly():
    return getSexAvgIntakeWeekly()

@router.get("/average/monthly")
async def get_intake_average_sex_monthly():
    return getSexAvgIntakeMonthly()

