from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from django.conf import settings 

DATABASE_URL= settings.DATABASE['default']['ENGINE']
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bird=engine)
session = Session ()
