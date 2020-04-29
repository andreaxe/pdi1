# coding=utf-8
from sqlalchemy import Column, DateTime, Float, String, Integer
import numpy as np
from datetime import datetime

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
# tutorial to create mysql docker and database schema
# https://medium.com/@johnathanfercher/mysql-docker-7ff6d50d6cf1


class ProductionType(Base):

    __tablename__ = 'production_type'

    country = Column(String(50), primary_key=True,)
    year = Column(Integer, primary_key=True)
    production_type = Column(String(80), primary_key=True)
    value = Column(Float)

    @staticmethod
    def save(df, range_dates, country):
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
        # todo convert all value columns to INT
        for year in years:
            pivot = df.pivot(index='country', columns='production_type', values=year)
            pivot['year'] = year
            print(pivot)
            pivot.to_sql('production_type', con=engine, if_exists='append', index=False)


class TotalLoad(Base):

    __tablename__ = 'total_load'

    country = Column(String(50), primary_key=True)
    datetime = Column(DateTime, primary_key=True)
    forecast = Column(Float)
    observed = Column(Float)

    @staticmethod
    def split_hour(value):
        """
        Returns the first half of time (ex: 00:00 - 01:00) returns 00:00
        :param value:
        :return:
        """
        return value.split(' ')[0]

    def save(self, df, day, country):
        country = country.split(" ", 1)[0]
        df['country'] = country
        df.columns = ['datetime', 'forecast', 'observed', 'country']
        df['datetime'] = df['datetime'].apply(self.split_hour)
        # drop nan values rows
        df = df.replace('n/e', np.NaN)
        df = df.replace('N/A', np.NaN)
        df = df.replace('n/a', np.NaN)
        df.dropna(inplace=True)
        if df.empty:
            return

        df['forecast'] = df['forecast'].astype(int)
        df['observed'] = df['observed'].astype(int)

        for i, row in df.iterrows():
            df['datetime'][i] = datetime.combine(datetime.strptime(day, '%d.%m.%Y+%H:%M').date(),
                                                 datetime.strptime(df['datetime'][i], '%H:%M').time())

        df.to_sql('total_load', con=engine, if_exists='append', index=False)
