from fastapi import FastAPI

from app.database import Base, engine
from app.routers import users, jobs, applications

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job Board API")

app.include_router(users.router)
app.include_router(jobs.router)
app.include_router(applications.router)


@app.get("/")
def root():
    return {"message": "Job Board API Running Successfully"}