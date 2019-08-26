"""
This creates the database schema, with the table name chore.
"""
from sqlalchemy import Column, Integer, String

#for configuration and class code
from sqlalchemy.ext.declarative import declarative_base

#for configuration
from sqlalchemy import create_engine

#create declarative_base instance
Base = declarative_base()

class Chores(Base):
    """ Chores class defines the table chore, with two columns chore_title and
    chore. It also gives an interface called serialze to return the json
    output with chore_title as key, and chore as value.
    """
    __tablename__ = 'chore'
    choreid = Column(Integer, primary_key=True)
    chore_title = Column(String(250), nullable=False)
    chore = Column(String(250), nullable=False)

    @property
    def serialize(self):
        return {
            self.chore_title : self.chore
        }

#creates a create_engine instance at the bottom of the file
engine = create_engine('sqlite:///chores-collection.db')
Base.metadata.create_all(engine)
