from fastapi import FastAPI
from api.routers import collaborator

app = FastAPI()

app.include_router(collaborator.router, prefix="/collaborators", tags=["collaborator"])

@app.get("/")
def root():
    return {"health_checked": True} 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)