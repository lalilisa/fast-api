from sqlalchemy.orm import Session
from sql.models import models
from sql.dtos import schemas

def create_user(db: Session, audio:schemas.AudioGenerated):
    db_audio = models.ManageAudioGenerated(audio)
    db.add(audio)
    db.commit()
    db.refresh(db_audio)
    return db_audio