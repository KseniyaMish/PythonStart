Table = {}

file = open(r'dataset_3380_5 (1).txt','r')
for i in file:
    line = i.strip().split()

    if len(line) != 3:
        continue

    class_number = int(line[0])
    height = int(line[2])

    if class_number in Table:
        Table[class_number]['sum'] += height
        Table[class_number]['counter'] += 1
    else:
        Table[class_number] = {
            'sum': height,
            'counter': 1,
        }

import json
print(json.dumps(Table,sort_keys=True, indent=4))
output = open(r'output_step5','w')
for i in range(1,12):
    if i in Table:
        avg = Table[i]['sum']/Table[i]['counter']
        output.write(str(i))
        output.write(' ')
        output.write(str(avg))
        output.write('\n')
    else:
        output.write(str(i))
        output.write(' -')
        output.write('\n')