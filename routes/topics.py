from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from typing import List
import schemas
from database import get_db
import services.topics
from typing import Optional


router = APIRouter()

@router.post("/", response_model=schemas.Topic)
def create_topic(
    name: str = Form(...), 
    chapter_id: int = Form(...), 
    details: Optional[str] = Form(None), 
    db: Session = Depends(get_db)
):
    print(f"Details received: {details}")
    topic = schemas.TopicCreate(name=name, details=details)
    
    db_topic = services.topics.create_topic(db=db, topic=topic, chapter_id=chapter_id)

    if not db_topic:
        raise HTTPException(status_code=400, detail="Chapter not found")
    return db_topic

@router.get("/", response_model=List[schemas.Topic])
def read_topics(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    topics = services.topics.get_topics(db, skip=skip, limit=limit)
    return topics

@router.get("/{topic_id}", response_model=schemas.Topic)
def read_topic(topic_id: int, db: Session = Depends(get_db)):
    db_topic = services.topics.get_topic(db=db, topic_id=topic_id)
    if db_topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    return db_topic
