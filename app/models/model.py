from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Record(Base):
    '''
    Record table
    The class of record table, store the information about keyword, url, result and last_modified time
    '''
    __tablename__ = 'record'
    id = Column(Integer, primary_key=True)
    word = Column(String(200))
    url = Column(Text)
    result = Column(Integer)
    last_modified = Column(String(200))
    query_date = Column(DateTime)

    def __init__(self, url, word, result=None, last_modified=None):
        '''
        Table schema
        Args:
            url (str): The url of website that need to be alalyzed
            word (str): The keyword that was used to analyzed
            result (int): How many times the keywords show up in website
            last_modified (str): HTTP last_modified of website
        '''
        self.word = word
        self.url = url
        self.result = result
        self.last_modified = last_modified
        self.query_date = datetime.utcnow()

    def add(self):
        '''
        Add a record to table
        '''
        session.add(self)
        session.commit()

    def query(self):
        '''
        Query a record from table
        '''
        out = session.query(Record).filter_by(
            word=self.word, url=self.url).first()
        if out is None:
            self.result = None
            self.last_modified = None
            self.query_date = None
        else:
            self.result = out.result
            self.last_modified = out.last_modified
            self.query_date = out.query_date


# Connect to sqlite db
engine = create_engine('sqlite:///db/record.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()