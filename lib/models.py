# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import relationship


# Base = declarative_base()

# class Task(Base):
#     __tablename__ = "tasks"

#     id = Column(Integer, primary_key=True)
#     name = Column(String(255), nullable=False)
#     description = Column(String(255))
#     due_date = Column(String(255))
#     status = Column(String(255))
#     task_list_id = Column(Integer, ForeignKey("task_lists.id"))

# class TaskList(Base):
#     __tablename__ = "task_lists"

#     id = Column(Integer, primary_key=True)
#     name = Column(String(255), nullable=False)

#     tasks = relationship("Task", backref="task_list")

# library/models.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    genre = Column(String)

    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}', genre='{self.genre}')>"
