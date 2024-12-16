from decimal import Decimal
from pydantic import BaseModel, Field
from typing import Optional
from api.schemas.collaborator.role_enum import RoleEnum


class UpdateCollaboratorSchema(BaseModel):
    role_code: Optional[RoleEnum] = Field(None, description="Code of the collaborator.")
    salary: Optional[Decimal] = Field(None, gt=1000, le=10000) 
    leader_code: Optional[str] = None

    class Config:
        use_enum_values = True 