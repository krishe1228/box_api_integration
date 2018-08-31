import ijson
import time

start = time.time()
filename = 'kris_data.json'
with open(filename, 'r') as f:
  objects = ijson.items(f,'entries.item')
  columns = list(objects)
  target_column = [col['source'] for col in columns]
  #target_column = [col['created_by'] for col in columns]
  good_columns = []
  for key,value in target_column[0].items():
    good_columns.append(key)

  #print(good_columns)

data = []
with open(filename, 'r') as f:
  for row in target_column: 
      selected_row = []
      for item in good_columns:
        selected_row.append(row.get(item))
      data.append(selected_row) 
print(good_columns)
#print(data)

runtime = time.time() - start
print('Run time: {}s'.format(round(runtime,4)))
