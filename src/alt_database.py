from sqlalchemy import create_engine, Column, String, Integer, delete
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

from settings import postgresql as pg_settings

#  init database

def get_engine(user, pswd, host, port, db):
    url = f'postgresql://{user}:{pswd}@{host}:{port}/{db}'
    if not database_exists:
        create_database(url)
    engine = create_engine(url, echo=False)
    return engine

def get_engine_from_settings():
    keys = ['pguser', 'pgpswd', 'pghost', 'pgport', 'pgdb']
    if not all(key in keys for key in pg_settings.keys()):
        raise Exception ('Bad config file')

    return get_engine(pg_settings['pguser'],pg_settings['pgpswd'],pg_settings['pghost'],pg_settings['pgport'],pg_settings['pgdb'])



engine = get_engine_from_settings()
conn = engine.connect()
Session = sessionmaker()
local_session = Session(bind=engine)

class RealEstate(Base):
    __tablename__ = 'real_estate'
    id = Column(Integer(), primary_key=True)
    image = Column(String(2000), nullable=True)
    title = Column(String(2000), nullable=True)
    location = Column(String(100), nullable=True)
    published_date = Column(String(50), nullable=True)
    bedrooms = Column(String(100), nullable=True)
    description = Column(String(2000), nullable=True)
    currency = Column(String(20), nullable=True)
    price = Column(String(100), nullable=True) 


Base.metadata.create_all(engine)

# clear current data (execute on init)
def clear_db():
    deleted = local_session.query(RealEstate).delete()
    print('deleted:', deleted)
    local_session.commit()


def add_data_to_database(data):
    try:
        local_session.add(
            RealEstate(
                image=data.get('image'),
                title=data.get('title'),
                location=data.get('location'),
                published_date=data.get('published_date'),
                bedrooms=data.get('bedrooms'),
                description=data.get('description'),
                currency=data.get('full_price')[0],
                price=data.get('full_price')[1]
            )
        )
        local_session.commit()
    except:
        print('ASDASDASDASDASDASAAAAADDDDDDDDDDDDDDDDDDDDDd')



data = local_session.query(RealEstate).all()
print(len(data), 'objects in db')
