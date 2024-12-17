from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Class(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    subjects = relationship("Subject", back_populates="class_")

class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    class_id = Column(Integer, ForeignKey("classes.id"))
    class_ = relationship("Class", back_populates="subjects")
    chapters = relationship("Chapter", back_populates="subject")

class Chapter(Base):
    __tablename__ = "chapters"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    subject = relationship("Subject", back_populates="chapters")
    topics = relationship("Topic", back_populates="chapter")

class Topic(Base):
    __tablename__ = "topics"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    details = Column(String, nullable=True)
    chapter_id = Column(Integer, ForeignKey("chapters.id"))
    chapter = relationship("Chapter", back_populates="topics")
