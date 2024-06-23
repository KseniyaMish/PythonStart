import sys
a = sys.argv
for i in range(1,len(a)):
    if a[i] == 0:
        continue
    else:
        print(a[i], end=' ')