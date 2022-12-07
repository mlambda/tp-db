from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

from .session import db_path, engine

Base = declarative_base()


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    capacity = Column(Integer)

    def __repr__(self) -> str:
        return (
            f"Location(id={self.id!r}, name={self.name!r}, capacity={self.capacity!r})"
        )


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(DateTime)
    location_id = Column(Integer, ForeignKey("locations.id"))
    location: Location = relationship("Location")

    def __repr__(self) -> str:
        return (
            f"Event(id={self.id!r}, name={self.name!r}, date={self.date!r}, "
            f"location={self.location!r})"
        )


db_path.unlink(missing_ok=True)
Base.metadata.create_all(engine)
