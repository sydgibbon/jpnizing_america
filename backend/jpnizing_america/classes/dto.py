from pydantic import BaseModel, EmailStr, ConfigDict
from typing import List

class classDTO(BaseModel):
    title = str
    video_url = str

class LevelDTO(BaseModel):
    level: str
    classes: List[classDTO]