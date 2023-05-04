from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .settings import SETTINGS

def get_engine(host, port, db, user, password):
    url = f'postgresql://{user}:{password}@{host}:{port}/{db}'
    return create_engine(url)

ENGINE = get_engine(**SETTINGS)
SESSIONFACTORY = sessionmaker(bind=ENGINE)