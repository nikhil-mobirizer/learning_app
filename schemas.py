from pydantic import BaseModel
from typing import Optional

class TopicBase(BaseModel):
    name: str
    details: Optional[str] = None
    
class TopicCreate(TopicBase):
    pass

class Topic(TopicBase):
    id: int
    chapter_id: int

    class Config:
        orm_mode = True

class ChapterBase(BaseModel):
    name: str
    subject_id: int

class ChapterCreate(ChapterBase):
    pass

class Chapter(ChapterBase):
    id: int
    subject_id: int
    topics: list[Topic] = []

    class Config:
        orm_mode = True

class SubjectBase(BaseModel):
    name: str

class SubjectCreate(SubjectBase):
    pass

class Subject(SubjectBase):
    id: int
    class_id: int
    chapters: list[Chapter] = []

    class Config:
        orm_mode = True

class ClassBase(BaseModel):
    name: str

class ClassCreate(ClassBase):
    pass

class Class(ClassBase):
    id: int
    subjects: list[Subject] = []

    class Config:
        orm_mode = True

