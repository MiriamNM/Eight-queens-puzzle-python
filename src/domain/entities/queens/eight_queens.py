
import uuid
from sqlalchemy import ARRAY, Column, Integer, String, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def uuid7():
    return str(uuid.uuid7())


class Queens(Base):
    __tablename__ = "queens"

    id = Column(UUID(as_uuid=True), primary_key=True,
                default=lambda: uuid7(), nullable=False)
    number_queens = Column(Integer, nullable=False)
    solutions = Column(ARRAY(String), nullable=False)
    created_by = Column(String(150), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_by = Column(String(150), nullable=True)
    updated_at = Column(DateTime, default=func.now(),
                        onupdate=func.now(), nullable=True)
