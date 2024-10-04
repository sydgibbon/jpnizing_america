from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from core.dao import BaseDAO
from models import Level
from dto import LevelDTO
from werkzeug.exceptions import BadRequest

class LevelDAO(BaseDAO):
    def get_Levels(self, db: Session, skip: int = 0, limit: int = 10):
        return self.select_all(Level, db, skip, limit)
    