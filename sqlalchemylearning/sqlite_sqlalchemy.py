"""
	There are three most important components in writing SQLAlchemy code:

		A Table that represents a table in a database.
		A mapper that maps a Python class to a table in a database.
		A class object that defines how a database record maps to a normal Python object.
"""

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Person(Base):

	__tablename__ = 'person'
	# Here we define columns for table person and each column is a normal python
	# instance attribte
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	
	
class Address(Base):

	__tablename__ = 'address'
	# Here we define columns for table address
	id =  Column(Integer, primary_key=True)
	street_name = Column(String(250))
	street_number = Column(String(250))
	post_code = Column(String(250), nullable=False)
	person_id = Column(Integer, ForeignKey('person.id'))
	person = relationship(Person)
	
# Create an engine that stores data in the local directory's test.db file

engine =  create_engine('sqlite:///test.db')

# Create all tables in the engine. This is equivalent to "Create Table" statement in rawsql

Base.metadata.create_all(engine)



