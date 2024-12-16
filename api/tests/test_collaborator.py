from fastapi.testclient import TestClient
from api.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.shared.database import Base
from unittest.mock import MagicMock

client = TestClient(app)

def setup_db():
    SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    return TestingSessionLocal

def test_create_collaborator():
    setup_db()

    data = {
    "first_name": "João",
    "last_name": "Silva",
    "registration_code": "12345",
    "role_code": "TL",
    "salary": 5000.0,
    "password": "senha1234!231"
    }


    response = client.post("/collaborators/", json=data)
    
    assert response.status_code == 201
    response_data = response.json()
    
    assert "collaborator_id" in response_data
    assert response_data["first_name"] == "João"
    assert response_data["last_name"] == "Silva"
    assert response_data["registration_code"] == "12345"
    assert response_data["salary"] == 5000.0

def test_find_collaborator():
    data = {
    "first_name": "Maria",
    "last_name": "Oliveira",
    "registration_code": "67890",
    "role_code": "TL",
    "salary": 7000.0,
    "password": "senha1234!231"
    }

    responseCreate = client.post("/collaborators/", json=data).json()
    response = client.get(f"/collaborators/{responseCreate['collaborator_id']}")
    assert response.status_code == 200
    data = response.json()
    assert responseCreate["collaborator_id"] == data['collaborator_id']
    assert responseCreate["first_name"] == data['first_name']
    assert responseCreate["last_name"] == data['last_name']
    assert responseCreate["registration_code"] == data['registration_code']
    
def test_get_all_collaborator():
    response = client.get("/collaborators")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_collaborator():
    data = {
    "first_name": "Carlos",
    "last_name": "Santos",
    "registration_code": "54321",
    "role_code": "TL",
    "salary": 8000.0,
    "password": "senha1234!231"
    }
    
    responseCreate = client.post("/collaborators/", json=data).json()

    dataUpdate = {
        "salary": 9001,
    }
    response = client.put(f"/collaborators/{responseCreate['collaborator_id']}", json=dataUpdate)
    assert response.status_code == 200
    data = response.json()
    data['salary'] == 9001
    
def test_delete_collaborator():    
    data = {
    "first_name": "Lucas",
    "last_name": "Pereira",
    "registration_code": "11223",
    "role_code": "TL",
    "salary": 7500.0,
    "password": "senha1234!231"
    }
    
    responseCreate = client.post("/collaborators/", json=data).json()
    response = client.delete(f"/collaborators/{responseCreate['collaborator_id']}")
    assert response.status_code == 204
    
def test_update_password_collaborator():
    data = {
    "first_name": "Ana",
    "last_name": "Costa",
    "registration_code": "98765",
    "role_code": "TL",
    "salary": 6500.0,
    "password": "senha1234!231"
    }

    
    responseCreate = client.post("/collaborators/", json=data).json()

    dataUpdate = {
        "password": "newPassword1212",
    }
    response = client.put(f"/collaborators/{responseCreate['collaborator_id']}/password", json=dataUpdate)
    assert response.status_code == 204
    
def test_update_status_collaborator():
    data = {
    "first_name": "Vanessa",
    "last_name": "Camargo",
    "registration_code": "9121765",
    "role_code": "TL",
    "salary": 4000.0,
    "password": "senha1234!231"
    }

    
    responseCreate = client.post("/collaborators/", json=data).json()

    dataUpdate = {
        "status_hired": False,
    }
    response = client.put(f"/collaborators/{responseCreate['collaborator_id']}/status", json=dataUpdate)
    assert response.status_code == 204
