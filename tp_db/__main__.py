from datetime import datetime

from pytz import timezone
from sqlalchemy import select

from .models import Event, Location
from .session import Session

with Session() as session, session.begin():
    cinematographe = Location(name="Cinématographe", capacity=300)
    cafe_du_commerce = Location(name="Café du Commerce", capacity=200)
    events = [
        Event(
            name="Club de Go",
            date=datetime(
                year=2022, month=12, day=7, hour=19, tzinfo=timezone("Europe/Paris")
            ),
            location=cafe_du_commerce,
        ),
        Event(
            name="Projection de Driver",
            date=datetime(
                year=2022, month=12, day=9, hour=19, tzinfo=timezone("Europe/Paris")
            ),
            location=cinematographe,
        ),
        Event(
            name="Projection de L'Honneur perdu de Katharina Blum",
            date=datetime(
                year=2022,
                month=12,
                day=10,
                hour=14,
                minute=45,
                tzinfo=timezone("Europe/Paris"),
            ),
            location=cinematographe,
        ),
    ]
    session.add_all(events)


with Session() as session:
    result = session.execute(
        select(Event).join(Location).where(Location.name == "Cinématographe")
    ).all()
    print(result)
