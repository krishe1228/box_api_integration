
response = requests.get('https://api.box.com/2.0/files/311955005962', headers=headers)
events_data = response.content
#print(event_data)
data = json.loads(events_data)
print_data = json.dumps(data, indent=4, sort_keys=True)
print(print_data)

