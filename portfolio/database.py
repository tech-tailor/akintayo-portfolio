from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from portfolio.models import *

engine = create_engine('sqlite:///portfolio.db', echo=True)
Base = declarative_base()

from portfolio.models import *

def init_db():
    Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

