from app.database import engine
from sqlalchemy import text

with engine.connect() as conn:
    conn.execute(text(
        "ALTER TABLE applications ADD COLUMN IF NOT EXISTS resume VARCHAR;"
    ))
    conn.commit()

print("Database updated successfully")