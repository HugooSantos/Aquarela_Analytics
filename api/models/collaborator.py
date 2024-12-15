from sqlalchemy import Column, BigInteger, String, ForeignKey, DECIMAL, Boolean, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from shared.database import Base

class Collaborator(Base):
    __tablename__ = 'collaborators'

    collaborator_id = Column(BigInteger, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    registration_code = Column(String(20), nullable=False)
    role_id = Column(BigInteger, ForeignKey('roles.role_id'), nullable=False)
    salary = Column(DECIMAL(10, 2), nullable=False)
    password = Column(String(255), nullable=False)
    status_hired = Column(Boolean, nullable=False)
    created_at = Column(TIMESTAMP(timezone=False), server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=False), server_default=func.now(), onupdate=func.now(), nullable=False)

    role = relationship("Role")

    
