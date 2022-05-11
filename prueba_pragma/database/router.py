from fastapi import APIRouter, HTTPException, Path, Depends
from config import sesion_local
from sqlalchemy.orm import Session
from schema import MicroBatchesSchema, Response
import service

router = APIRouter()

def conection_db():
  db = sesion_local()
  try:
    yield db
  finally:
    db.close()
    
    
@router.post('/create')
async def create(request:MicroBatchesSchema, db:Session=Depends(conection_db)):
  print("PARAMETERS",request)
  service.create_data(db, request.parameter)
  return Response(code=200, status="OK", message="Create").dict(exclude_none=True)
