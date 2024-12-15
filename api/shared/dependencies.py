from .database import SessionLocal, engine, Base
from sqlalchemy_utils import database_exists, create_database

def get_db():
    check_db_exist()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def check_db_exist():        
    print(engine.url)
    if not database_exists(engine.url):
        create_database(engine.url)
        Base.metadata.create_all(bind=engine)