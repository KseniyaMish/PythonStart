line = []

with open(r'C:\Users\kmish\Downloads\dataset_3363_3 (9).txt', 'r') as file1:
    for i in file1:
        line = file1.read().replace('\n', ' ').lower().split()
        line = sorted(line)

count = 0
current = ''
word = ''
C = 0

for row in line:
    print(row)
    if row != current:
        if count > C or (count == C and current < word):
            C = count
            word = current
        current = row
        count = 0
    else:
        count += 1

if count > C:
    word = current



print(C+1, word, 'hey')
