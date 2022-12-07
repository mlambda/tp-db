from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_path = Path("events.db")

engine = create_engine(f"sqlite:///{db_path}", echo=True, future=True)

Session = sessionmaker(engine)
