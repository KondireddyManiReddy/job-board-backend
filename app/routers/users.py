from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import schemas, models
from app.database import get_db
from app.security import (
    hash_password,
    verify_password,
    create_access_token
)


# Do NOT add prefix here
# main.py already has /users prefix
router = APIRouter(
    tags=["Users"]
)


# =====================
# Register User
# =====================

@router.post(
    "/register",
    response_model=schemas.UserResponse
)
def register(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = models.User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        role="user"
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user



# =====================
# Login User
# =====================

@router.post(
    "/login",
    response_model=schemas.Token
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    db_user = db.query(models.User).filter(
        models.User.email == form_data.username
    ).first()


    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )


    if not verify_password(
        form_data.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Incorrect password"
        )


    token = create_access_token(
        {
            "sub": str(db_user.id),
            "email": db_user.email,
            "role": db_user.role
        }
    )


    return {
        "access_token": token,
        "token_type": "bearer"
    }