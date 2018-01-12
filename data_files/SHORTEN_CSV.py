import csv


lines = []
with open('COMMON_WORDS.txt', 'r') as f:
    for line in f.readlines():
        l = line
        l = l.replace('\n', '')
        lines.append(l)


output = open('SHORT_NO_VERBS.csv', 'w', newline="\n", encoding="utf-8")
writer = csv.writer(output)

already_visited_list = []

with open ('FULL_THESAURUS.csv', 'rt') as f:
    reader = csv.reader(f)
    field_names_list = next(reader)
    writer.writerow(field_names_list)

    for row in reader:
        if (row[0] not in already_visited_list) & (row[0] in lines) & (str(row[2]) != "(noun)"):
            writer.writerow(row)
            already_visited_list.append(row[0])
