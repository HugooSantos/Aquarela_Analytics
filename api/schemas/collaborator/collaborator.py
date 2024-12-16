from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CollaboratorSchema(BaseModel):
    collaborator_id: int
    first_name: str
    last_name: str
    registration_code: str
    leader_name: Optional[str]
    leader_code: Optional[str]
    role_id: int
    salary: float
    status_hired: bool
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
