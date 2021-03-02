from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from src.settings import *

engine = create_engine(SQLITE_DB_PATH, convert_unicode=True)

db_session = scoped_session(sessionmaker(
	autocommit=False,
	autoflush=False,
	bind=engine
))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
	from src.models import Car

	Base.metadata.create_all(bind=engine)
