from typing import TYPE_CHECKING

from sqlalchemy import MetaData

if TYPE_CHECKING:
    from sqlalchemy import Engine

def delete_table(tablename: str, engine: "Engine") -> None:
    meta = MetaData()
    meta.reflect(bind=engine)
    meta.tables[tablename].drop(engine)