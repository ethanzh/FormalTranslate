import csv

with open('final_short.csv', 'r') as f:
    reader = csv.reader(f)

    print(list(reader)[3612][3])
