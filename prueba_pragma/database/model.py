
from sqlalchemy import Column, Integer, String
from config import base

class MicroBatches(base):
  __tablename__ = 'test'
  
  timestamp = Column(String, primary_key=True)
  price = Column(Integer)
  user_id = Column(Integer) 
  execution_time = Column(String)