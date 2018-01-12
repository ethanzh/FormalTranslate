import csv

with open('FINAL_SHORT_ALL_POS.csv', 'r') as f:
    reader = csv.reader(f)

    for i in range(0, len(list(reader[0]))):
		if str(word) == str(list(reader[0])):
			print(list(reader[0][i]))
	
