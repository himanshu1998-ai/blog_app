from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

from .database import Base, engine


class Blog(Base):
    __tablename__ = "blogs"

    blog_id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    Date = Column(DateTime, default=func.now())
    creator = relationship("User", back_populates="blogss")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    Date = Column(DateTime, default=func.now())
    blogss = relationship('Blog', back_populates="creator")


Base.metadata.create_all(engine)
