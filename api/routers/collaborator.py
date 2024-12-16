from fastapi import APIRouter, Depends
from api.schemas.collaborator.change_password_collaborator import ChangePasswordCollaboratorSchema
from api.schemas.collaborator.change_status_collaborator import ChangeStatusCollaboratorSchema
from api.schemas.collaborator.collaborator import CollaboratorSchema
from api.schemas.collaborator.create_collaborator import CreateCollaboratorSchema
from api.schemas.collaborator.update_collaborator import UpdateCollaboratorSchema
from api.services import collaborator_service
from typing import List
from sqlalchemy.orm import Session
from api.shared.dependencies import get_db

router = APIRouter()


@router.get("/", response_model=List[CollaboratorSchema], status_code=200)
def get_all(db: Session = Depends(get_db)) -> List[CollaboratorSchema]:
    
    """
    Retrieve all collaborators from the system.

    - **db**: The database session used to interact with the database.

    This endpoint returns a list of all collaborators in the system.
    """
    
    return collaborator_service.get_all(db=db)


@router.get("/{collaborator_id}", response_model=CollaboratorSchema, status_code=200)
def find(collaborator_id: int,
         db: Session = Depends(get_db)) -> CollaboratorSchema:
    
    """
    Retrieve a collaborator by their ID.

    - **collaborator_id**: The ID of the collaborator to find.
    - **db**: The database session used to interact with the database.

    This endpoint returns the details of a single collaborator based on the given ID.
    If the collaborator with the provided ID is not found, an error will be raised.
    """
    
    return collaborator_service.find(db=db, collaborator_id=collaborator_id)


@router.post("/", response_model=CollaboratorSchema, status_code=201)
def create(schema: 
    CreateCollaboratorSchema,
    db: Session = Depends(get_db))-> CollaboratorSchema:
    
    """
    Create a new collaborator in the system.

    - **schema**: The data to create a new collaborator.
    - **db**: The database session used to interact with the database.

    This endpoint accepts the collaborator's data and returns the created collaborator.
    """
    
    return collaborator_service.create(db=db, schema=schema)
    
    
@router.put("/{collaborator_id}", response_model=CollaboratorSchema)
def update(collaborator_id: int, 
           schema: UpdateCollaboratorSchema, 
           db: Session = Depends(get_db)) -> CollaboratorSchema:
    
    """
    Update the details of an existing collaborator in the system.

    - **collaborator_id**: The ID of the collaborator to update.
    - **schema**: The data to update the collaborator's information.
    - **db**: The database session used to interact with the database.

    This endpoint accepts the collaborator's ID and updated data, 
    then returns the updated collaborator's details. 
    If the collaborator is not found, a 404 error is returned.
    """
    
    return collaborator_service.update(db=db, 
                                       collaborator_id=collaborator_id,
                                       schema=schema)


@router.delete("/{collaborator_id}", status_code=204)
def delete(collaborator_id: int, db: Session = Depends(get_db)) -> None:
    
    """
    Delete a collaborator by their ID.

    - **collaborator_id**: The ID of the collaborator to delete.
    - **db**: The database session used to interact with the database.

    This endpoint deletes a collaborator with the given ID. If the collaborator 
    is not found, a 404 error is returned.
    """
    
    return collaborator_service.delete(db=db,
                                       collaborator_id=collaborator_id)


@router.put("/{collaborator_id}/password", status_code=204)
def change_password(collaborator_id: int, 
           schema: ChangePasswordCollaboratorSchema, 
           db: Session = Depends(get_db)) -> None:
    
    """
    Update the password of an existing collaborator in the system.
    
    - **collaborator_id**: The ID of the collaborator whose password is being updated.
    - **schema**: The new password data for the collaborator.
    - **db**: The database session used to interact with the database.
    
    This endpoint accepts the collaborator's ID and new password data, 
    then updates the password for the collaborator. 
    If the collaborator is not found, a 404 error is returned.
    """
    
    return collaborator_service.change_password(db=db, 
                                       collaborator_id=collaborator_id,
                                       schema=schema)
    
@router.put("/{collaborator_id}/status", status_code=204)
def change_status(collaborator_id: int, 
           schema: ChangeStatusCollaboratorSchema, 
           db: Session = Depends(get_db)) -> None:
    
    """
    Update the status of an existing collaborator in the system.
    
    - **collaborator_id**: The ID of the collaborator whose status is being updated.
    - **schema**: The new status data for the collaborator.
    - **db**: The database session used to interact with the database.
    
    This endpoint accepts the collaborator's ID and new status data, 
    then updates the status for the collaborator. 
    If the collaborator is not found, a 404 error is returned.
    """
    
    return collaborator_service.change_status(db=db, 
                                       collaborator_id=collaborator_id,
                                       schema=schema)