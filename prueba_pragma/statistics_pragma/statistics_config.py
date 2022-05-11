import  psycopg2
from dotenv import load_dotenv
import os

def connection_database():
  load_dotenv()
  ip = os.getenv('ip')
  port = os.getenv('port')
  password = os.getenv('password')
  user = os.getenv('user')
  database = os.getenv('database')

  connection = psycopg2.connect(
      database=database,
      user=user,
      password=password,
      host=ip,
      port=port    
  )
  
  return connection