import requests
import json
import time
from auth import authenticate

start = time.time()
_,access_token,refresh_token = authenticate()
auth_str = 'Bearer ' + access_token
print(auth_str)
headers = {
    'Authorization': auth_str,
}

params = (
    ('stream_type', 'all'),
    ('stream_position', '0'),
    ('limit', '500'),
)

response = requests.get('https://api.box.com/2.0/events', headers=headers, params=params)
events_data = response.content
#print(events_json)
data = json.loads(events_data)
print_data = json.dumps(data, indent=4, sort_keys=True)
print(print_data)

with open('kris_data.json','w') as outfile:
    #json.dump(data, outfile)
    outfile.write(json.dumps(data, indent=4, sort_keys=True))

runtime = time.time() - start
print('Run time: {}s'.format(round(runtime,4)))
