from typing import Dict, List, Tuple
from api.models.collaborator import Collaborator
from api.models.role import Role
from api.schemas.collaborator.update_collaborator import UpdateCollaboratorSchema
from sqlalchemy.orm import Session

def get_all(db: Session) -> List[Collaborator]:
    return db.query(Collaborator).all()

def create(db: Session, collaborator_dict: Dict) -> Collaborator:
    collaborator = Collaborator(**collaborator_dict)
    db.add(collaborator)
    db.commit()
    db.refresh(collaborator)
    return collaborator

def get_by_id(db: Session, collaborator_id: int) -> Collaborator:
    return db.query(Collaborator).get(collaborator_id)

def update(db: Session,
           collaborator: Collaborator) -> Collaborator:
    db.commit()
    db.refresh(collaborator)
    return collaborator

def delete(db: Session, collaborator:Collaborator) -> None:
    db.delete(collaborator)
    db.commit()
    
def get_by_registration_code(db: Session, collaborator_code: str) -> Tuple:
    return db.query(Collaborator, Role).\
        join(Role, Collaborator.role_id == Role.role_id).\
        filter(Collaborator.registration_code == collaborator_code).\
        first()
