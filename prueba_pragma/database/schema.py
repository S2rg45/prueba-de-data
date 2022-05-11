from typing import Generic, List, Optional, TypeVar
from unittest import result
from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar('T')


class MicroBatchesSchema(BaseModel):
  parameter: Optional[dict]=None
  timestamp: Optional[str]=None
  price: Optional[int]=None
  user_id: Optional[int]=None
  execution_time: Optional[str]=None
  
  class Config:
    orm_mode = True
  
  
class Response(GenericModel, Generic[T]):
  code: Optional[int]=None
  status: Optional[str]=None
  messages: Optional[str]=None
  result: Optional[T]