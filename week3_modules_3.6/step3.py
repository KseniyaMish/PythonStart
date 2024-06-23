import requests
first = open('dataset_3378_3.txt', 'r')
line = first.readline().strip()
first.close()

file = requests.get('https://stepik.org/media/attachments/course67/3.6.3/699991.txt')
s = file.text
while True:
    if s[0] != "W":
        print(s, s[0])
        file = requests.get('https://stepik.org/media/attachments/course67/3.6.3/'+s)
        s = file.text
    else:
        print(s, s[0])
        A = s.strip()
        break

