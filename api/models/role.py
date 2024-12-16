from enum import Enum
from sqlalchemy import Column, BigInteger, String, Boolean
from api.shared.database import Base
from enum import Enum


class RoleEnum(int, Enum):
    JD = 1
    MD = 2
    SD = 3
    TL = 4

        
class Role(Base):
    __tablename__ = 'roles'
    role_id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(40), nullable=False)
    role_code = Column(String(40), nullable=False)
    can_lead = Column(Boolean, nullable=False)
