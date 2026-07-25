from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas, models
from app.database import get_db


router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


# Get all jobs
@router.get("/")
def get_jobs(
    db: Session = Depends(get_db)
):
    return db.query(models.Job).all()



# Get single job
@router.get("/{job_id}", response_model=schemas.JobResponse)
def get_job(
    job_id: int,
    db: Session = Depends(get_db)
):

    job = db.query(models.Job).filter(
        models.Job.id == job_id
    ).first()


    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    return job



# Create job
@router.post("/", response_model=schemas.JobResponse)
def create_job(
    job: schemas.JobCreate,
    db: Session = Depends(get_db)
):

    new_job = models.Job(
        title=job.title,
        company=job.company,
        location=job.location,
        description=job.description
    )


    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job



# Update job
@router.put("/{job_id}", response_model=schemas.JobResponse)
def update_job(
    job_id: int,
    job_data: schemas.JobCreate,
    db: Session = Depends(get_db)
):

    job = db.query(models.Job).filter(
        models.Job.id == job_id
    ).first()


    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )


    job.title = job_data.title
    job.company = job_data.company
    job.location = job_data.location
    job.description = job_data.description


    db.commit()
    db.refresh(job)

    return job



# Delete job
@router.delete("/{job_id}")
def delete_job(
    job_id: int,
    db: Session = Depends(get_db)
):

    job = db.query(models.Job).filter(
        models.Job.id == job_id
    ).first()


    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )


    db.delete(job)
    db.commit()


    return {
        "message": "Job deleted successfully"
    }