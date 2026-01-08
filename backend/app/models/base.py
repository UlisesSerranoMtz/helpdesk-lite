from peewee import Model
from app.core.db import db

class BaseModel(Model):
    class Meta:
        database = db