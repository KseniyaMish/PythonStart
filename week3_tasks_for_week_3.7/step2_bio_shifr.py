def Making_shifr(B):
    n = ''
    strok = ''
    for i in B:
        n = Shifr[i]
        strok = strok + n
    return (strok)
def Unmaking_shifr(B1):
    n = ''
    strok = ''
    for i in B1:
        n = Shifr1[i]
        strok = strok + n
    return (strok)

Shifr = {}
Shifr1 = {}
count = 0
A = input() # исходный алфавит
A1 = input() # закодированный алфавит
for i in A:
    Shifr[i] = A1[count]
    count += 1
count = 0
for i in A1:
    Shifr1[i] = A[count]
    count += 1


B = input()
B = Making_shifr(B)
print(B)

B1 = input()
B1 = Unmaking_shifr(B1)
print(B1)