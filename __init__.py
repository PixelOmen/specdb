from typing import TYPE_CHECKING, Union

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if TYPE_CHECKING:
    from sqlalchemy.engine import Engine
    from sqlalchemy.orm.session import Session

ENGINE: Union["Engine", None] = None
SESSIONFACTORY: sessionmaker["Session"] | None = None

def start_engine(host, port, db, user, password) -> None:
    global ENGINE, SESSIONFACTORY
    if ENGINE is not None and SESSIONFACTORY is not None:
        return
    url = f'postgresql://{user}:{password}@{host}:{port}/{db}'
    ENGINE = create_engine(url)
    SESSIONFACTORY = sessionmaker(bind=ENGINE)

def get_session() -> "Session":
    global SESSIONFACTORY
    if SESSIONFACTORY is None:
        raise Exception("Cannot get session, Database engine not started.")
    return SESSIONFACTORY()