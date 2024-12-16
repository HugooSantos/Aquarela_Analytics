from ast import Dict
from typing import List
from fastapi import HTTPException
from api.models.collaborator import Collaborator
from api.models.role import RoleEnum
from api.repositories import collaborator_repository
from api.schemas.collaborator.change_password_collaborator import ChangePasswordCollaboratorSchema
from api.schemas.collaborator.change_status_collaborator import ChangeStatusCollaboratorSchema
from api.schemas.collaborator.create_collaborator import CreateCollaboratorSchema
from api.schemas.collaborator.update_collaborator import UpdateCollaboratorSchema
from sqlalchemy.orm import Session

from api.utils.security import hash_password


def get_all(db: Session) -> List[Collaborator]:
    return collaborator_repository.get_all(db)

def find(db: Session, collaborator_id: int) -> Collaborator:
    collaborator = collaborator_repository.get_by_id(db=db,
                                                     collaborator_id=collaborator_id) 
    
    if collaborator is None:
        raise HTTPException(status_code=404, detail="Collaborator not found")
    
    return collaborator

def create(db: Session, schema: CreateCollaboratorSchema) -> Collaborator:
    collaborator_dict = schema.dict()
    check_leader_can_append(db, collaborator_dict)
    check_can_be_lead(collaborator_dict)
    role_code_data = set_role_code(collaborator_dict)
    collaborator_dict['status_hired'] = True
    collaborator_dict['password'] = hash_password(collaborator_dict['password'])
    collaborator_dict.update(role_code_data)
    return collaborator_repository.create(db, collaborator_dict)

def check_leader_can_append(db: Session, collaborator_dict: Dict) -> None:
    if collaborator_dict["leader_code"] is None:
        return
    
    leader = collaborator_repository.get_by_registration_code(db, collaborator_dict['leader_code'])
    
    if leader is None:
        raise HTTPException(status_code=400, detail="Leader code invalid")
    
    collaborator, role = leader
    can_lead = role.can_lead
    
    if not can_lead:
        raise HTTPException(status_code=400, 
                            detail="".join([
                                    "The collaborator's leader role ",
                                    "does not grant leadership permissions."
                                          ]))
    
def check_can_be_lead(collaborator_dict:Dict) -> None:
    if collaborator_dict["leader_code"] is not None:
        return
    
    role_cod = collaborator_dict['role_code']  
    if role_cod != 'TL':
        raise HTTPException(status_code=400, 
                            detail="The collaborator's cannot lead, please set leader code.")
        

def set_role_code(collaboratorSchema_dict:Dict) -> Dict:
    role_cod = collaboratorSchema_dict['role_code']  
    role_id = RoleEnum[role_cod].value
    collaboratorSchema_dict['role_id'] = role_id
    collaboratorSchema_dict.pop('role_code', None)
    return collaboratorSchema_dict

def update(db, collaborator_id:int,
           schema:UpdateCollaboratorSchema) -> Collaborator:
    collaborator = find(db=db, collaborator_id=collaborator_id)
    collaborator_dict = schema.dict()
    check_can_improve_salary(collaborator_dict, collaborator)
    check_leader_can_append(db,collaborator_dict)
    role_code_data = check_can_improve_job(collaborator_dict, collaborator)
    
    if role_code_data is not None:
        collaborator_dict.update(role_code_data)
    
    for key, value in collaborator_dict.items():
        setattr(collaborator, key, value) 
    return collaborator_repository.update(db=db,
                                      collaborator=collaborator) 
    
def check_can_improve_salary(collaborator_dict: Dict, collaborator: Collaborator) -> None:
    if collaborator_dict["salary"] is None:
        return
    
    check = collaborator_dict['salary'] > collaborator.salary 
    if check:
        return
    
    raise HTTPException(status_code=400, 
                            detail="The promotion salary must be higher.")

def check_can_improve_job(collaborator_dict: Dict, collaborator: Collaborator) -> None:
    if collaborator_dict['role_code'] is None:
        return
    
    dict = set_role_code(collaborator_dict)
    
    if dict['role_id'] > collaborator.role_id:
        return
    
    raise HTTPException(status_code=400, 
                            detail="The promotion role code must be higher.")
    
def delete(db, collaborator_id:int) -> None:
   collaborator = find(db=db, collaborator_id=collaborator_id)
   collaborator_repository.delete(db=db,
                                  collaborator=collaborator) 

def change_password(db, collaborator_id:int, schema:ChangePasswordCollaboratorSchema) -> None:
   collaborator = find(db=db, collaborator_id=collaborator_id)
   collaborator_dict = schema.dict()
   collaborator.password = hash_password(collaborator_dict['password'])
   
   collaborator_repository.update(db=db,
                                  collaborator=collaborator) 
   
def change_status(db, collaborator_id:int, schema:ChangeStatusCollaboratorSchema) -> None:
   collaborator = find(db=db, collaborator_id=collaborator_id)
   collaborator_dict = schema.dict()
   collaborator.status_hired = collaborator_dict['status_hired']   
   collaborator_repository.update(db=db,
                                  collaborator=collaborator) 