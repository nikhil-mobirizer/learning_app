from fastapi import APIRouter, Depends, HTTPException, Form
from typing import List
import schemas
from database import get_db
import services.chapters
router = APIRouter()
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

@router.post("/", response_model=schemas.Chapter)
def create_chapter(
    subject_id: int = Form(...),  # Parse subject_id from the form data
    name: str = Form(...),       # Parse chapter name from the form data
    db: Session = Depends(get_db)
):
    chapter = schemas.ChapterCreate(name=name)
    db_chapter = services.chapters.create_chapter(db=db, chapter=chapter, subject_id=subject_id)
    
    if not db_chapter:
        raise HTTPException(status_code=400, detail="Subject not found")
    return db_chapter

@router.get("/", response_model=List[schemas.Chapter])
def read_chapters(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    chapters = services.chapters.get_chapters(db, skip=skip, limit=limit)
    return chapters

@router.get("/{chapter_id}", response_model=schemas.Chapter)
def read_chapter(chapter_id: int, db: Session = Depends(get_db)):
    db_chapter = services.chapters.get_chapter(db=db, chapter_id=chapter_id)
    if db_chapter is None:
        raise HTTPException(status_code=404, detail="Chapter not found")
    return db_chapter

@router.get("/subject/{subject_id}", response_class=JSONResponse)
async def get_chapters_by_subject(subject_id: int, db: Session = Depends(get_db)):
    chapters = services.chapters.get_chapters_by_subject(db, subject_id)
    print("-----------", chapters)
    if not chapters:
        raise HTTPException(status_code=404, detail="Chapters not found")
    return chapters
