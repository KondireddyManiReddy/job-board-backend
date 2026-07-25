from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db


router = APIRouter(
    prefix="/applications",
    tags=["Applications"]
)


@router.get("/")
def get_applications(db: Session = Depends(get_db)):
    return db.query(models.Application).all()


@router.post("/", response_model=schemas.ApplicationResponse)
def create_application(
    application: schemas.ApplicationCreate,
    db: Session = Depends(get_db)
):

    new_application = models.Application(
        job_id=application.job_id,
        user_id=application.user_id,
        resume=application.resume,
        status="Applied"
    )

    db.add(new_application)
    db.commit()
    db.refresh(new_application)

    return new_application