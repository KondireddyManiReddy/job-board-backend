from pydantic import BaseModel


# =====================
# User Schemas
# =====================

class UserCreate(BaseModel):
    name: str
    email: str
    password: str



class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str

    class Config:
        from_attributes = True



class UserLogin(BaseModel):
    email: str
    password: str



class Token(BaseModel):
    access_token: str
    token_type: str



# =====================
# Job Schemas
# =====================

class JobCreate(BaseModel):
    title: str
    company: str
    location: str
    description: str



class JobResponse(BaseModel):
    id: int
    title: str
    company: str
    location: str
    description: str

    class Config:
        from_attributes = True



# =====================
# Application Schemas
# =====================

class ApplicationCreate(BaseModel):
    job_id: int
    user_id: int
    resume: str



class ApplicationResponse(BaseModel):
    id: int
    job_id: int
    user_id: int
    resume: str
    status: str

    class Config:
        from_attributes = True