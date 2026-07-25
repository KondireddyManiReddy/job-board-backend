from app.database import SessionLocal
from app import models

db = SessionLocal()

db.query(models.User).filter(
    models.User.email == "mani@gmail.com"
).delete()

db.commit()

db.close()

print("User deleted")