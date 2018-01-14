from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlite_sqlalchemy import Person, Address, Base


engine = create_engine('sqlite:///test.db')

# Bind the engine to the metadata of the base class so that the declaratives can
# be accessed through a DB session
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the database session 
# object. Any change made against the objects in the session won't be persisted
# into the database until you call session.commit(). If you're not happy about the
# changes, you can revert all of them back to the last commit by calling
# session.rollback()

session = DBSession()

# Insert a record into Person table
new_person = Person(name='Nathan Waksmen')
session.add(new_person)
session.commit()

# Insert a record into Address table
new_address = Address(post_code='345678', person=new_person)
session.add(new_address)
session.commit()
