from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os


load_dotenv()
ip = os.getenv('ip')
port = os.getenv('port')
password = os.getenv('password')
user = os.getenv('user')
database = os.getenv('database')

DATABASE_URL = f'postgresql://{user}:{password}@{ip}:{port}/{database}'
engine = create_engine(DATABASE_URL)
sesion_local = sessionmaker(autocommit=False, autoflush=True, bind=engine)
base = declarative_base()