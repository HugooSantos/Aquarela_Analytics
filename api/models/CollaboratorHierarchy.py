
from api.shared.database import Base
from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.orm import relationship

class CollaboratorHierarchy(Base):
    __tablename__ = 'collaborator_hierarchy'
    
    hierarchy_id = Column(BigInteger, primary_key=True)
    subordinate_id = Column(BigInteger, ForeignKey('collaborators.collaborator_id'), nullable=False)
    supervisor_code = Column(String(40))
    
    subordinate = relationship('Collaborator')
    supervisor = relationship('Role')