from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    Float,
    Integer,
    String,
)
from sqlalchemy.ext.declarative import DeclarativeMeta

db = SQLAlchemy()

BaseModel: DeclarativeMeta = db.Model


class TimingResult(BaseModel):
    id = Column(BigInteger, primary_key=True)
    date_created = Column(DateTime, nullable=False)
    group = Column(String(40))
    number_of_exercises = Column(Integer)
    used_time = Column(Float)

    def __repr__(self):
        return f"""<TimingResult id = {self.id}, 
    date_created = {self.date_created},
    group = "{self.name}",
    number_of_exercises = {self.number_of_exercises},
    used_time = {self.used_time}>"""