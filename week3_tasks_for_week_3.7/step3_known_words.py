A = int(input())
A1 = {}
for i in range(A):
    word = input().lower()
    A1[word] = ''
    print(word)

B = int(input())
B1 = {}
for i in range(B):
    new_word = input().lower().split()
    for i in new_word:
        if i not in A1:
            B1[i] = ''
for i in B1:
    print(i)
