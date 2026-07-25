from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


# =====================
# User Model
# =====================

class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    email = Column(
        String,
        unique=True,
        index=True,
        nullable=False
    )

    password = Column(
        String,
        nullable=False
    )

    role = Column(
        String,
        default="user"
    )

    applications = relationship(
        "Application",
        back_populates="user"
    )



# =====================
# Job Model
# =====================

class Job(Base):
    __tablename__ = "jobs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String,
        nullable=False
    )

    company = Column(
        String,
        nullable=False
    )

    location = Column(
        String,
        nullable=False
    )

    description = Column(
        String,
        nullable=False
    )

    applications = relationship(
        "Application",
        back_populates="job"
    )



# =====================
# Application Model
# =====================

class Application(Base):
    __tablename__ = "applications"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    job_id = Column(
        Integer,
        ForeignKey("jobs.id")
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    resume = Column(
        String
    )

    status = Column(
        String,
        default="Applied"
    )


    job = relationship(
        "Job",
        back_populates="applications"
    )


    user = relationship(
        "User",
        back_populates="applications"
    )