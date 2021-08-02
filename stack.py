
# Import into Jupyter
import csv
from csv import DictReader
import time



def readData():
    
    read_obj = csv.reader(open('Data/data.csv', 'r'))
    for row in read_obj:
        for x in row:
            print(abs(int(float(x))))


while True:
    readData()
