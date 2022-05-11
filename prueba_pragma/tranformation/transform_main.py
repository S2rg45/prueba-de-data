import requests
import json
from datetime import datetime

from statistics_pragma import statistics_main



def transform_data(data_csv , number_batch):
  format_data = data_csv.values.tolist()
  parts_data = [format_data[i:i + number_batch] for i in range(0, len(format_data), number_batch)]
  for datas in parts_data:
      for item in datas:
        current_date = datetime.now()
        date_string = current_date.strftime("%m/%d/%Y, %H:%M:%S")
        items = {'parameter':{'timestamp': item[0],'price': item[1], 'user_id': item[2], 'execution_time': date_string}}
        print(items)  
        send_parameters(items)
        statistics_main.get_data()
        
                    
def send_parameters(item):
    save_data = requests.post('http://localhost:8000/data/create', data=json.dumps(item)) 
    response = save_data
    print(response)
    # sleep(1)
  
            
