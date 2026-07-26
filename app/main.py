from fastapi import FastAPI



# Import your routers (if you have them)
from app.routers import users, jobs, applications


app = FastAPI(
    title="Job Board API",
    version="1.0.0"
)


# Create database tables
# models.Base.metadata.create_all(bind=engine)


# Health check
@app.get("/")
def home():
    return {
        "message": "Job Board API is running"
    }


# Register API routes
app.include_router(
    users.router,
    prefix="/users",
    tags=["Users"]
)

app.include_router(
    jobs.router,
    prefix="/jobs",
    tags=["Jobs"]
)

app.include_router(
    applications.router,
    prefix="/applications",
    tags=["Applications"]
)