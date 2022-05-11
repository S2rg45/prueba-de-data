from time import sleep
from intake import read_data as data


while True:
  print("****************************")
  print("***Pipeline Sergio Moreno***")
  print("****************************")
  validation = data.read_csv()
  if validation == False:
    print("****************************")
    print("****En espera por datos*****")
    print("****************************")
    sleep(10)
  else:
    break