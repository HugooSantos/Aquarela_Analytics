from decimal import Decimal
from pydantic import BaseModel, Field
from typing import Optional
from api.schemas.collaborator.role_enum import RoleEnum


class CreateCollaboratorSchema(BaseModel):
    first_name: str = Field(..., max_length=50)
    last_name: str = Field(..., max_length=50)
    registration_code: str = Field(..., max_length=20)
    role_code: RoleEnum = Field(..., description="code of collaborator.")
    salary: Decimal = Field(..., gt=1000, le=10000)  
    password: str = Field(..., max_length=255)
    leader_name: Optional[str] = None  
    leader_code: Optional[str] = None  

    class Config:
        use_enum_values = True 