
from sqlalchemy.orm import Session
from model import MicroBatches
from schema import MicroBatchesSchema

def create_data(db: Session, data: MicroBatchesSchema):
  _data = MicroBatches(timestamp=data['timestamp'], price=data['price'], user_id=data['user_id'], execution_time=data['execution_time'])
  db.add_all([_data])
  db.commit()
  db.refresh(_data)
  return _data
