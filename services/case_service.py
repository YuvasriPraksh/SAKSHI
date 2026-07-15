# services/case_service.py

from datetime import datetime, timezone
from uuid import uuid4

from fastapi import HTTPException

from database import supabase
from schemas.case_schema import (
    CaseCreateRequest,
    CaseCreateResponse,
    CaseUpdateRequest,
    CaseResponse,
    CaseListResponse,
)

TABLE_NAME = "cases"


def create_case(payload: CaseCreateRequest) -> CaseCreateResponse:
    now = datetime.now(timezone.utc).isoformat()
    case_id = f"CASE-{uuid4().hex[:8].upper()}"

    record = payload.model_dump()
    record["assigned_officer"] = str(record["assigned_officer"])
    record.update(
        {
            "case_id": case_id,
            "created_at": now,
            "updated_at": now,
        }
    )

    try:
        response = supabase.table(TABLE_NAME).insert(record).execute()
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Failed to create case: {exc}")

    if not response.data:
        raise HTTPException(status_code=500, detail="Case creation failed")

    return CaseCreateResponse(
        message="Case created successfully",
        case=CaseResponse(**response.data[0]),
    )


def get_all_cases() -> CaseListResponse:
    try:
        response = supabase.table(TABLE_NAME).select("*").execute()
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Failed to fetch cases: {exc}")

    cases = [CaseResponse(**row) for row in response.data]
    return CaseListResponse(total_cases=len(cases), cases=cases)


def get_case_by_id(case_id: str) -> CaseResponse:
    try:
        response = (
            supabase.table(TABLE_NAME)
            .select("*")
            .eq("case_id", case_id)
            .execute()
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Failed to fetch case: {exc}")

    if not response.data:
        raise HTTPException(status_code=404, detail="Case not found")

    return CaseResponse(**response.data[0])


def update_case(case_id: str, payload: CaseUpdateRequest) -> CaseResponse:
    update_data = payload.model_dump(exclude_unset=True)

    if not update_data:
        raise HTTPException(status_code=400, detail="No fields provided to update")

    if "assigned_officer" in update_data and update_data["assigned_officer"] is not None:
        update_data["assigned_officer"] = str(update_data["assigned_officer"])

    update_data["updated_at"] = datetime.now(timezone.utc).isoformat()

    try:
        response = (
            supabase.table(TABLE_NAME)
            .update(update_data)
            .eq("case_id", case_id)
            .execute()
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Failed to update case: {exc}")

    if not response.data:
        raise HTTPException(status_code=404, detail="Case not found")

    return CaseResponse(**response.data[0])