import ijson
import time

start = time.time()

preview_dict = {}
filename = 'kris_data.json'
with open(filename, 'r') as f:
  objects = ijson.items(f,'entries.item')
  columns = list(objects)
  for item in columns:
    term = item['event_type']
    if term == 'COMMENT_CREATE':
      item_id = item['source']['item']['id']
      item_type = item['source']['item']['type']
      created_time = item['created_at']
      item_owner = item['created_by']['name']
      comment_creator = item['source']['created_by']['name']
      comment_message = item['source']['message']
      if preview_dict.get(item_owner) == None:
        #preview_dict[item_owner] = ['','','']
        preview_dict[item_owner] = [[item_id, item_type, created_time, comment_creator, comment_message]]
      else:
        preview_dict[item_owner].append([item_id, item_type, created_time, comment_creator, comment_message])

print(preview_dict)

for key, value in preview_dict.items():
  for row in value:
    print('{} created a comment on {} ID: {},owned by {} at {}, message: {}'.format(row[3], row[1], row[0], key, row[2], row[4]))

runtime = time.time() - start
print('Run time: {}s'.format(round(runtime, 4)))
