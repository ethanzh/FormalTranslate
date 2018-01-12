import csv

with open('thes.csv', 'r') as f:
    reader = csv.reader(f)

    print(list(reader)[198645][3])
