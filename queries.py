# coding=utf-8

# 1 - imports
from models.base import Session, Base, engine
from models.total_load import TotalLoadActualLoad, TotalLoadDayAhead
from models.MyModel import ProductionType

# 2 - extract a session
session = Session()
Base.metadata.create_all(engine)


# 3 - extract all movies
movies = session.query(TotalLoadActualLoad).all()

def save_total_day_ahead(df):
    pass
# 4 - print movies' details
# print('\n### All movies:')
# for movie in movies:
#     print(f'{movie.title} was released on {movie.release_date}')
# print('')
