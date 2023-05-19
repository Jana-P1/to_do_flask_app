from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlite3, click

engine = create_engine('sqlite:///test.db')
db_session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
  ))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    print("The Database")
    from myapplication.models.models import User, ToDo
    
    Base.metadata.create_all(bind=engine)


