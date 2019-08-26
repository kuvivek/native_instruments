"""
This is for the chores-collection db creation
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#Let's import our Chores and Base classes from our database_setup.py file
from database_setup import Base

engine = create_engine('sqlite:///chores-collection.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a dbsession instance
Base.metadata.bind = engine

dbsession = sessionmaker(bind=engine)
# A dbsession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object.
session = dbsession()
