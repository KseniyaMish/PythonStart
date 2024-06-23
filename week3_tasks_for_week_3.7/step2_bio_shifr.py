def making_shifr(A):
    strok = ''
    for i in A:
        n = ''
        if i == 'a':
            n = '*'
        elif i == 'b':
            n = 'd'
        elif i == 'd':
            n = '#'
        elif i == 'c':
            n = '%'
        strok = strok + n
    return(strok)

def unmaking_shifr(A):
    strok = ''
    for i in A:
        n = ''
        if i == '*':
            n = 'a'
        if i == 'd':
            n = 'b'
        if i == '#':
            n = 'd'
        if i == '%':
            n = 'c'
        strok = strok + n
    return(strok)
A = input()
A = input()

A = input()
A = making_shifr(A)
print(A)

A = input()
A = unmaking_shifr(A)
print(A)