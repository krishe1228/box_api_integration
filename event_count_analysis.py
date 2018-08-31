import ijson
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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

#counter = 1 
#for line in target_column: 
#  print('{} {}'.format(counter, line))
#  counter += 1

sources_df = pd.DataFrame(data, columns = good_columns)
#print(sources)
print(sources_df['name'].value_counts())
sources_type_col_lst = sources_df['name'].value_counts().keys().tolist()
sources_type_count_lst = sources_df['name'].value_counts().tolist()
#print(sources_type_col_lst)
#print(sources_type_count_lst)

#plot_data = pd.DataFrame({'col_lst': sources_type_col_lst, 'count_lst': sources_type_count_lst})
# visualization
plt.figure(figsize=(15,6))
sns.barplot(x=sources_type_col_lst, y=sources_type_count_lst)
plt.xticks(rotation= 45)
plt.xlabel(' FileType')
plt.ylabel('Count')
plt.title('Box Content')
plt.show()

runtime = time.time() - start
print('Run time: {}s'.format(round(runtime,4)))
