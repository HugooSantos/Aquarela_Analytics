from decimal import Decimal
from pydantic import BaseModel, Field
from typing import Optional
from api.schemas.collaborator.role_enum import RoleEnum


class ChangePasswordCollaboratorSchema(BaseModel):
    password: str = Field(..., max_length=255)

    class Config:
        use_enum_values = True 