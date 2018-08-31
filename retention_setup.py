import requests

headers = {
    'Authorization': 'Bearer 2xNYGJG94Slh3SG9EQIMr0TzCD3TPuK3',
}

data = '{"policy_name": "KrisRetentionPolicy", "policy_type": "finite", "retention_length": 365, "disposition_action": "remove_retention"}'

response = requests.post('https://api.box.com/2.0/retention_policies', headers=headers, data=data)
events_data = response.content
print(events_data)
