import csv

lines = []
with open('try.txt', 'r') as f:
    for line in f.readlines():
        l = line
        l = l.replace('\n', '')
        lines.append(l)


output = open('new.csv', 'w', newline="\n", encoding="utf-8")
writer = csv.writer(output)


already_visited = []

toy = []


with open ('thesaurus.csv', 'rt') as f:
    reader = csv.reader(f)
    field_names_list = next(reader)
    writer.writerow(field_names_list)
    #print(field_names_list)
    for row in reader:
          #if "test suit" == row[0]: # if the username shall be on column 3 (-> index 2)
          #    print("Is in file")
          #if row[0] not in lines:
          #    print("not here")
          if row[0] not in already_visited:
              if row[0] in lines:
                  writer.writerow(row)
                  toy.append(row)
                  already_visited.append(row[0])


text_file = open("Output.txt", "w")
text_file.write(str(toy))
text_file.close()
