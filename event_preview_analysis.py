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
    if term == 'ITEM_PREVIEW' or term == 'ITEM_OPEN':
      item_name = item['source']['name']
      previewed_time = item['created_at']
      previewed_by = item['created_by']['name']
      item_owner = item['source']['created_by']['name']
      if preview_dict.get(item_owner) == None:
        #preview_dict[item_owner] = ['','','']
        preview_dict[item_owner] = [[item_name, previewed_time, previewed_by]]
      else:
        preview_dict[item_owner].append([item_name, previewed_time, previewed_by])


      #print('Item Name: {}'.format(item_name))
      #print('Item Owner: {}'.format(item_owner))
      #print('Previewd at: {}'.format(previewed_time))
      #print('Previewd by: {}'.format(previewed_by))
      #print()
print(preview_dict)

for key, value in preview_dict.items():
  for row in value:
    print('{} previewed {} at {} owned by {}'.format(row[2], row[0], row[1], key))

runtime = time.time() - start
print('Run time: {}s'.format(round(runtime, 4)))
