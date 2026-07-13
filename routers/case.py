from fastapi import APIRouter

router = APIRouter()

# Create a new POCSO case
@router.post("/create-case")
def create_case():
    return {
        "message": "Case Created Successfully"
    }

# View all cases
@router.get("/cases")
def get_cases():
    return {
        "cases": [
            {
                "case_id": "POCSO001",
                "district": "Chennai",
                "status": "Medical Pending"
            }
        ]
    }

# View timeline of a case
@router.get("/timeline")
def get_timeline():
    return {
        "case_id": "POCSO001",
        "current_stage": "Medical Examination"
    }

# Update current stage
@router.post("/update-stage")
def update_stage():
    return {
        "message": "Stage Updated Successfully"
    }