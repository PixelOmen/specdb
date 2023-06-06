from typing import TYPE_CHECKING, Callable

from . import ENGINE
from .schema import Spec, TempSpec, Client

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

def init_db() -> None:
    Client.__table__.create(ENGINE, checkfirst=True)
    Spec.__table__.create(ENGINE, checkfirst=True)

def delete_client(client_name: str, session: "Session") -> None:
    client = session.query(Client).filter(Client.name == client_name).first()
    if client is None:
        return
    for spec in client.specs:
        session.delete(spec)
    session.delete(client)

def spec_to_temp(transferfunc: Callable[[Spec], TempSpec], session: "Session") -> None:
    TempSpec.__table__.drop(ENGINE, checkfirst=True)
    TempSpec.__table__.create(ENGINE)
    allspecs = session.query(Spec).all()
    for spec in allspecs:
        tempspec = transferfunc(spec)
        session.add(tempspec)

def temp_to_spec(session: "Session") -> None:
    Spec.__table__.drop(ENGINE, checkfirst=True)
    Spec.__table__.create(ENGINE)
    alltempspecs = session.query(TempSpec).all()
    for tempspec in alltempspecs:
        spec = Spec(**tempspec.columns())
        session.add(spec)