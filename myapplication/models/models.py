from myapplication.db import Base, init_db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(75), index=True)
    email = Column(String(100), index=True, unique=True)
    password_hash = Column(String(128))
    posts = Column(Integer, ForeignKey("todos.id"))

    def __init__(self, username, email, password):
        self.usernamne = username
        self.email = email
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.name!r}>'
    
    
class ToDo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    owner = Column(Integer, ForeignKey("users.id"), nullable=False)
    description = Column(String(128), nullable=False)
    date = Column(DateTime())

    def __init__(self, owner, description, date):
        self.owner = owner
        self.description = description
        self.date = date


    def __repr__(self):
        return f'<ToDOs: Description: {self.description} -- Date: {self.date}>'