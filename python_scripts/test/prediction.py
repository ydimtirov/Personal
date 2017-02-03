import requests
import json
url = 'http://localhost:9000/api'
data = json.dumps({'preg':6, 'plas':148, 'pres': 72, 'skin': 35, 'test':0, 'mass':33.6, 'pedi':0.627, 'age':50})
r = requests.post(url, data)
print r.json()