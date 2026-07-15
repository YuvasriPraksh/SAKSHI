# schemas/case_schema.py

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class CaseBase(BaseModel):
    case_type: str
    district: str
    police_station: str
    assigned_officer: UUID
    current_stage: str
    status: str


class CaseCreateRequest(CaseBase):
    pass


class CaseUpdateRequest(BaseModel):
    case_type: Optional[str] = None
    district: Optional[str] = None
    police_station: Optional[str] = None
    assigned_officer: Optional[UUID] = None
    current_stage: Optional[str] = None
    status: Optional[str] = None


class CaseResponse(CaseBase):
    case_id: str
    created_at: datetime
    updated_at: datetime


class CaseListResponse(BaseModel):
    total_cases: int
    cases: list[CaseResponse]


class CaseCreateResponse(BaseModel):
    message: str
    case: CaseResponse