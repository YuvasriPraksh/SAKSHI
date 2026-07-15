# routers/case.py

from fastapi import APIRouter

from schemas.case_schema import (
    CaseCreateRequest,
    CaseCreateResponse,
    CaseUpdateRequest,
    CaseResponse,
    CaseListResponse,
)
from services.case_service import (
    create_case,
    get_all_cases,
    get_case_by_id,
    update_case,
)

router = APIRouter(tags=["Case Management"])


@router.post("/create-case", response_model=CaseCreateResponse)
def create_case_endpoint(payload: CaseCreateRequest):
    return create_case(payload)


@router.get("/cases", response_model=CaseListResponse)
def list_cases_endpoint():
    return get_all_cases()


@router.get("/cases/{case_id}", response_model=CaseResponse)
def get_case_endpoint(case_id: str):
    return get_case_by_id(case_id)


@router.put("/cases/{case_id}", response_model=CaseResponse)
def update_case_endpoint(case_id: str, payload: CaseUpdateRequest):
    return update_case(case_id, payload)