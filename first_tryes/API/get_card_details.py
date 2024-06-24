import pprint

import requests

headers = {'Authorization': 'Basic dXNlcm5hbWU6cS5oU2c1KVAke3JLUUBwcSU7TiVdSjQ7Vn5eL11oQTU='}
params = {'id': '92c07eb6-c707-4d5c-bec4-5a9f7215a333'}
A = requests.get('https://sm-api.getdisco.dev/spending/v1/bank/cards/'+params['id'], headers=headers)
if A.status_code == 200:
    print('200')
for i in A:
    print(i)
