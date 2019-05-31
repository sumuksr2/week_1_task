# The purprose of this program is to show my knowledge of the GET and POST Request methods.
# I used two different APIs to test this knowledge.

import requests
import json

requests.get('https://github.com')

r = requests.get('http://swapi.co/api/people/1')
print(r.json())

p = requests.post('https://enyy7edz20pnr.x.pipedream.net', data={'name': 'John Doe'})
print(p.status_code)

data = json.dumps({'name': 'newrepo', 'description': 'a test repo'})
g = requests.post('https://api.github.com/user/repos', data=data, auth=('sumuksrao', '*********'))
print(g.json())