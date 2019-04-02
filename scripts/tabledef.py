import sys
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

#=======================Database initialization======================
SQLALCHEMY_DATABASE_URI = 'sqlite:///fake.db'

Base = declarative_base()

#======================function to create a connection to a Database===============
def db_connect():
    return create_engine(SQLALCHEMY_DATABASE_URI)


#=====================Function to create a Database using ORM====================
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column("Admin_name", String(30), unique=True)
    password = Column("Admin_password", String(30), nullable=False)
    email = Column("Admin_email", String(50), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

engine = db_connect()  # Connect to database
Base.metadata.create_all(engine)  # Create models
