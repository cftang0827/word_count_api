from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///record.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class Record(Base):
    __tablename__ = 'record'
    id = Column(Integer, primary_key=True)
    word = Column(String(200))
    result = Column(Integer)
    last_modified = Column(String(200))
    query_date = Column(DateTime)

    def __init__(self, word, result, last_modified):
        self.word = word
        self.result = result
        self.last_modified = last_modified
        self.query_date = datetime.utcnow()
