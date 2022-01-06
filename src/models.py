import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(200),unique=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(200),nullable=False)
    email = Column (String, unique=True)
    login_password = Column (String(200))
    followers_relation = relationship("Follower")
    sharers_relation= relationship("Share")
    posts_relation = relationship("Post")


class Post(Base):
    __tablename__ = 'posts'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id= Column(Integer,ForeignKey('users.id'), primary_key=True)
    user_id = Column(Integer, unique = True)
    media_relation = relationship("Media")
    likes_relation=relationship("Like")
    comments_relation=relationship("Comment")

class Media(Base):
    __tablename__ = 'medias'
    id= Column(Integer,ForeignKey('posts.id'), primary_key=True)
    type= Column(String(200))
    url = Column (String(200))
    post_id = Column(Integer, unique=True)

class Like(Base):
    __tablename__ = 'likes'
    user_id = Column(Integer,ForeignKey('posts.id'), primary_key=True)
    post_id = Column(Integer, unique=True)
    comment_id= Column(Integer, unique=True)
    author_id= Column(Integer, unique=True)

class Comment(Base):
    __tablename__ = 'comments'
    id= Column(Integer,ForeignKey('posts.id'),primary_key=True)
    comment = Column(Text(1000))
    author_id= Column(Integer)
    post_id= Column(Integer)

class Follower(Base):
    __tablename__='followers'
    id= Column(Integer,ForeignKey('users.id') ,primary_key=True)
    username = Column(Integer, primary_key=True)
    user_id= Column(Integer,unique=True)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e