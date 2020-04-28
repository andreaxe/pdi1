# coding=utf-8
from sqlalchemy import Column, DateTime, Float, String
from models.base import Base


class TotalLoadDayAhead(Base):

    __tablename__ = 'total_load_day_ahead'

    country = Column(String(50), primary_key=True)
    datetime_start = Column(DateTime, primary_key=True)
    datetime_end = Column(DateTime)
    value = Column(Float)

    def __init__(self, country, datetime_start, datetime_end, value):

        self.country = country
        self.datetime_start = datetime_start
        self.datetime_end = datetime_end
        self.value = value


class TotalLoadActualLoad(Base):

    __tablename__ = 'total_load_actual_load'

    country = Column(String(50), primary_key=True)
    datetime_start = Column(DateTime, primary_key=True)
    datetime_end = Column(DateTime)
    value = Column(Float)

    def __init__(self, country, datetime_start, datetime_end, value):

        self.country = country
        self.datetime_start = datetime_start
        self.datetime_end = datetime_end
        self.value = value
