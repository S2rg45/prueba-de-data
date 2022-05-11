from itertools import count
from time import sleep
from unicodedata import name
from numpy import number
import pandas as pd
import os
from random import randrange


from tranformation import transform_main as transform_data


def read_csv():
    count_file = os.listdir('../dataPruebaDataEngineer/')
    if len(count_file) != 0:
      number_batch = randrange(1, 10)
      for file in count_file:
        name_file = file.split(".")
        if name_file[0] != 'validation':
          data_csv = pd.read_csv(f'../dataPruebaDataEngineer/{file}')
          transform_data.transform_data(data_csv=data_csv, number_batch=number_batch)
        else:
          data_csv_validation = pd.read_csv(f'../dataPruebaDataEngineer/{file}')
          transform_data(data_csv_validation, number_batch)
          return True
    else:
      return False
    

# if __name__ == '__main__':
#   read_csv()

