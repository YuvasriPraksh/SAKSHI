from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard")
def dashboard():
    return {
        "total_cases": 120,
        "pending_cases": 25,
        "completed_cases": 95,
        "delayed_cases": 10
    }