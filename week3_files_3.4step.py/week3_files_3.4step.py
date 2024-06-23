math = 0
physics = 0
language = 0
Avg = 0
count = 0
rowc = 0

file = open(r'dataset_3363_4 (1).txt','r')
for row in file:
    row = row.strip().split(';')
    for element in row:
        if count >= 1:
            Avg += int(row[count])
            if count == 1:
                math += int(row[count])
            elif count == 2:
                physics += int(row[count])
            elif count == 3:
                language += int(row[count])
        count += 1
    count = 0
    Avg = Avg/3
    output = open(r'Output.py.txt','a')
    output.write(str(Avg))
    output.write('\n')
    rowc += 1
    Avg = 0

output.write(str(math/rowc))
output.write(' ')
output.write(str(physics/rowc))
output.write(' ')
output.write(str(language/rowc))
output.write(' ')



