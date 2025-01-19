import uuid
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Queens(Base):
    __tablename__ = "queens"

    id = Column(UUID(as_uuid=True), primary_key=True,
                default=uuid.uuid4, nullable=False)
    number_queens = Column(Integer, nullable=False)
    solutions = Column(ARRAY(String), nullable=False)

    def to_dict(self):
        return {
            "id": str(self.id),
            "number_queens": self.number_queens,
            "solutions": self.solutions,
        }
