from decimal import Decimal
from pydantic import BaseModel, Field
from typing import Optional
from api.schemas.collaborator.role_enum import RoleEnum


class ChangeStatusCollaboratorSchema(BaseModel):
    status_hired: bool
    class Config:
        use_enum_values = True 