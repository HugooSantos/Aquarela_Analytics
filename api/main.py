from fastapi import FastAPI
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/")
def root():
    return {"health_checked": True} 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)