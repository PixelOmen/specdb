from typing import TYPE_CHECKING

from sqlalchemy import MetaData
from .schema import Spec, Client

if TYPE_CHECKING:
    from sqlalchemy import Engine
    from sqlalchemy.orm import Session

def delete_table(tablename: str, engine: "Engine") -> None:
    meta = MetaData()
    meta.reflect(bind=engine)
    meta.tables[tablename].drop(engine, checkfirst=True)

def delete_client(clientname: str, session: "Session") -> None:
    client = session.query(Client).filter(Client.name == clientname).first()
    if client is None:
        return
    session.delete(client)
    session.commit()

def delete_spec(specname: str, session: "Session") -> None:
    spec = session.query(Spec).filter(Spec.name == specname).first()
    if spec is None:
        return
    session.delete(spec)
    session.commit()
