from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from typing import List
import schemas
from database import get_db
import services.classes

router = APIRouter()

@router.post("/", response_model=schemas.Class)
def create_class(name: str = Form(...), db: Session = Depends(get_db)):
    class_ = schemas.ClassCreate(name=name)
    return services.classes.create_class(db=db, class_=class_)

@router.get("/", response_model=List[schemas.Class])
def read_classes(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    classes = services.classes.get_classes(db, skip=skip, limit=limit)
    return classes

@router.get("/{class_id}", response_model=schemas.Class)
def read_class(class_id: int, db: Session = Depends(get_db)):
    db_class = services.classes.get_class(db=db, class_id=class_id)
    if db_class is None:
        raise HTTPException(status_code=404, detail="Class not found")
    return db_class
