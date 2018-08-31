import ijson
import time

start = time.time()
# collab_dict = {collab_id: [object_id, object_name, object_accessor, count]}
owner_dict = {}
collab_dict = {}
file_name = 'kris_data.json'
with open(file_name, 'r') as f:
  objects = ijson.items(f,'entries.item')
  columns = list(objects)
  #source_column = [col['source'] for col in columns]
  for item in columns: 
    if item['source']['type'] == 'collaboration':
      #print(item)
      object_name = item['source']['item']['name']
      object_type = item['source']['item']['type']
      object_id = item['source']['item']['id']
      object_owner = item['source']['created_by']['name']
      collab_id = item['source']['id']
      try:
        object_accessor = item['source']['accessible_by']['name']
      except TypeError:
        object_accessor = ''
      if object_accessor != '':
        if owner_dict.get(collab_id) == None:
          collab_dict[collab_id] = ['','','','',0]
        collab_dict[collab_id] = [object_id, object_name, object_owner, object_accessor, 0]
        if item['event_type'] == 'COLLAB_INVITE_COLLABORATOR':
          collab_dict[collab_id][4] += 1
        elif item['event_type'] == 'COLLAB_ROLE_CHANGE':
          collab_dict[collab_id][1] = object_name
        elif item['event_type'] == 'COLLAB_REMOVE_COLLABORATOR':
          collab_dict[collab_id][4] -= 1

for key, value in collab_dict.items():
  #print(value)
  if owner_dict.get(value[2]) == None:
    owner_dict[value[2]] = []
  if value[4] == 1:
    owner_dict[value[2]].append([value[0], value[1], value[3]])

print(owner_dict)
print()

#for k, v in owner_dict.items():
#  for i in v:
#    print('{} owns collaboration object {} accessible by {}'.format(k, i[1], i[2]))

runtime = time.time() - start
print('Run time: {}s'.format(round(runtime,4)))
