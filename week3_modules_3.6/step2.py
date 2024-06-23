import requests

file1 = open (r'dataset_3378_2.txt','r')
line = file1.readline().strip()
print(line)
count = 0

r = requests.get('https://stepik.org/media/attachments/course67/3.6.2/895.txt',params='count()')
print(r.text.count('\n'))


