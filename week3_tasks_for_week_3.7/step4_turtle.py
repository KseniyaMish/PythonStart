A = int(input())
x = 0
y = 0

for i in range(A):
    a = input().split()
    if a[0] == 'восток':
        x += int(a[1])
    elif a[0] == 'север':
        y += int(a[1])
    elif a [0] == 'запад':
        x -= int(a[1])
    else:
        y -= int(a[1])

print(x, y)