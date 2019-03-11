from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Record(Base):
    __tablename__ = 'record'
    id = Column(Integer, primary_key=True)
    word = Column(String(200))
    url = Column(Text)
    result = Column(Integer)
    last_modified = Column(String(200))
    query_date = Column(DateTime)

    def __init__(self, url, word, result=None, last_modified=None):
        self.word = word
        self.url = url
        self.result = result
        self.last_modified = last_modified
        self.query_date = datetime.utcnow()

    def add(self):
        session.add(self)
        session.commit()

    def query(self):
        out = session.query(Record).filter_by(word=self.word, url=self.url).first()
        self.result = out.result
        self.last_modified = out.last_modified
        self.query_date = out.query_date


engine = create_engine('sqlite:///db/record.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()