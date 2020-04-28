# coding=utf-8
from sqlalchemy import Column, DateTime, Float, String, Integer
import pandas as pd

# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db.sqlite')
Session = sessionmaker(bind=engine)
Base = declarative_base()
Base.metadata.create_all(bind=engine)

# tutorial to teach how to use sqlalchemy and pandas
# https://www.dataquest.io/blog/sql-insert-tutorial/


class ProductionType(Base):

    __tablename__ = 'production_type'

    country = Column(String(50), primary_key=True,)
    year = Column(Integer, primary_key=True)
    production_type = Column(String(80), primary_key=True)
    value = Column(Float)

    def save(self, df, range_dates, country):
        """
        Clean the dataframe
        :param df: the pandas dataframe
        :param range_dates: tuple of dates
        :param country: string
        :return:
        """
        country = country.split(" ", 1)[0]
        years = [year for year in (range(range_dates[0].year, range_dates[1].year + 1))]
        header = ['production_type'] + years
        df.columns = header
        df['country'] = country
        for year in years:
            pivot = df.pivot(index='country', columns='production_type', values=year)
            pivot['year'] = year
            print(pivot)
            pivot.to_sql('production_type', con=engine, if_exists='append')

# class TotalLoad(Base):
#     pass
