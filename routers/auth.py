from fastapi import APIRouter, Header

from schemas.login_schema import (
    LoginRequest,
    LoginResponse,
    OTPVerifyRequest,
    OTPVerifyResponse,
)
from schemas.role_schema import RoleResponse

from services.auth_service import (
    authenticate_user,
    verify_otp,
    get_role,
)

router = APIRouter(
    tags=["Authentication"]
)


@router.post(
    "/login",
    response_model=LoginResponse,
    summary="Officer Login"
)
def login(login: LoginRequest):
    return authenticate_user(login)


@router.post(
    "/verify-otp",
    response_model=OTPVerifyResponse,
    summary="Verify Officer OTP"
)
def verify_otp_endpoint(data: OTPVerifyRequest):
    return verify_otp(data)


@router.get(
    "/role",
    response_model=RoleResponse,
    summary="Get Officer Role"
)
def role(access_token: str = Header(...)):
    return get_role(access_token)