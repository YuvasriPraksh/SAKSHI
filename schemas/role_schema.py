from pydantic import BaseModel


class RoleResponse(BaseModel):
    officer_name: str
    role: str
    permissions: list[str]