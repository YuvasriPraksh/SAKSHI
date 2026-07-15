from fastapi import HTTPException

from schemas.login_schema import (
    LoginRequest,
    LoginResponse,
    OTPVerifyRequest,
    OTPVerifyResponse,
)
from schemas.role_schema import RoleResponse

# ---------------------------------------------------------------------------
# Dummy officer data (to be replaced with database records later)
# ---------------------------------------------------------------------------
DUMMY_EMAIL = "police@tn.gov.in"
DUMMY_PASSWORD = "police123"
DUMMY_OTP = "123456"
DUMMY_OFFICER_NAME = "Inspector Arjun"
DUMMY_ROLE = "Police Officer"
DUMMY_ACCESS_TOKEN = "dummy_access_token"

# Dummy Role Permissions
ROLE_PERMISSIONS = {
    "Police Officer": [
        "Create Case",
        "Update Timeline",
        "View Dashboard",
        "View Cases",
    ],
    "Admin": [
        "Create Case",
        "Update Timeline",
        "View Dashboard",
        "View Cases",
        "Manage Officers",
    ],
}


# -----------------------------
# Login Service
# -----------------------------
def authenticate_user(login: LoginRequest) -> LoginResponse:
    if login.email == DUMMY_EMAIL and login.password == DUMMY_PASSWORD:
        return LoginResponse(
            message="OTP sent successfully",
            otp_required=True,
            email=login.email,
        )

    raise HTTPException(
        status_code=401,
        detail="Invalid Email or Password"
    )


# -----------------------------
# OTP Verification Service
# -----------------------------
def verify_otp(data: OTPVerifyRequest) -> OTPVerifyResponse:
    if data.otp == DUMMY_OTP:
        return OTPVerifyResponse(
            message="Login Successful",
            officer_name=DUMMY_OFFICER_NAME,
            role=DUMMY_ROLE,
            access_token=DUMMY_ACCESS_TOKEN,
        )

    raise HTTPException(
        status_code=401,
        detail="Invalid OTP"
    )


# -----------------------------
# Role Validation Service
# -----------------------------
def get_role(access_token: str) -> RoleResponse:
    if access_token != DUMMY_ACCESS_TOKEN:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired access token"
        )

    permissions = ROLE_PERMISSIONS.get(DUMMY_ROLE)

    if permissions is None:
        raise HTTPException(
            status_code=403,
            detail="Role not authorized"
        )

    return RoleResponse(
        officer_name=DUMMY_OFFICER_NAME,
        role=DUMMY_ROLE,
        permissions=permissions,
    )