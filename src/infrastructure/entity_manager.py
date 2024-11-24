import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database_url = os.getenv("DATABASE_URL")

engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
