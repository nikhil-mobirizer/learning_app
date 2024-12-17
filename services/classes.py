from sqlalchemy.orm import Session
from models import Class
from schemas import ClassCreate
from fastapi import HTTPException

def get_class(db: Session, class_id: int):
    return db.query(Class).filter(Class.id == class_id).first()

def get_classes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Class).offset(skip).limit(limit).all()

def create_class(db: Session, class_: ClassCreate):
    # Check for duplicate class name
    existing_class = db.query(Class).filter(Class.name == class_.name).first()
    if existing_class:
        raise HTTPException(status_code=400, detail="Class already exists")

    # Create new class
    db_class = Class(name=class_.name)
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class
