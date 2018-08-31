import ijson
import time

start = time.time()
owner_dict = {}
folder_dict = {}
file_name = 'kris_data.json'
with open(file_name, 'r') as f:
  objects = ijson.items(f,'entries.item')
  columns = list(objects)
  #source_column = [col['source'] for col in columns]
  for item in columns: 
    if item['source']['type'] == 'folder':
      folder_name = item['source']['name']
      folder_owner = item['source']['owned_by']['name']
      folder_id = item['source']['id']
      event_type = item['event_type']
      
      if folder_dict.get(folder_id) == None:
        folder_dict[folder_id] = [folder_owner, folder_name, 0]
      
      if event_type == 'ITEM_CREATE':
        folder_dict[folder_id][2] += 1
      elif event_type == 'ITEM_RENAME':
        folder_dict[folder_id][1] = folder_name
      elif event_type == 'ITEM_TRASH':
        folder_dict[folder_id][2] -= 1


for k,v in folder_dict.items():
  if v[2] == 1:
    folder_owner = v[0]
    if owner_dict.get(folder_owner) == None:
      owner_dict[folder_owner] = [] 
    owner_dict[folder_owner].append(folder_dict[k][1]) 

print(owner_dict)
#print(folder_dict)
runtime = time.time() - start
print('Run time: {}s'.format(round(runtime,4)))
