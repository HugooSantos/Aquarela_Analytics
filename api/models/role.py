from sqlalchemy import Column, BigInteger, String, Boolean
from api.shared.database import Base

class Role(Base):
    __tablename__ = 'roles'
    role_id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(40), nullable=False)
    role_code = Column(String(40), nullable=False)
    can_lead = Column(Boolean, nullable=False)
