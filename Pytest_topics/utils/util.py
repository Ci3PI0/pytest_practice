import csv
from pathlib import Path

datafile = 'data.csv'
cfgFileDirectory = 'config'

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR.joinpath(cfgFileDirectory).joinpath(datafile)
print(BASE_DIR)
print(DATA_FILE)

def get_data():
    with open(DATA_FILE,"+r") as f:
        reader = csv.reader(f)
        next(reader) ## Пропуск первой строки
        data = [tuple(row) for row in reader]
        return data


# data = get_data()
# for e in data:
#     print(f'ID:{e[0]}')
#     print(f'NAME:{e[1]}')
#     print(f'COURSE:{e[2]}')
#     print(f'COUNTRY:{e[3]}')
# print(data)