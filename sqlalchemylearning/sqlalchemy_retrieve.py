from sqlite_sqlalchemy import Person, Base, Address
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///test.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

# Make a query to find all personin the database
person_list = session.query(Person).all()

for person_obj in person_list:
	print("Person name:", person_obj.name)

address_list = session.query(Address).all()

for add_obj in address_list:
	print("Address of "+ add_obj.person.name + " is : "+add_obj.post_code)
