

lines = []
with open('Output.txt', 'r') as f:
    for line in f.readlines():
        l = line
        #l = l.replace('\n', '')
        lines.append(l)

print(lines[0][3])
