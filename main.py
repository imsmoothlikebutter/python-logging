import logging
import datetime
from time import sleep
import os


f = open("./test.log", "a")

if os.path.isfile('./test.log'):
    logging.basicConfig(filename=f'./test.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
    while True:
        current_date_time = datetime.datetime.now()
        formatted_date_time = current_date_time.strftime('%Y-%m-%d-%H%M%S')
        logging.info(f'{formatted_date_time} - This is a log message')
        sleep(5)




 
