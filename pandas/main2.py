# https://chrisalbon.com/python/data_wrangling/pandas_dataframe_importing_csv/
# https://stackoverflow.com/questions/32011359/convert-categorical-data-in-pandas-dataframe
# https://stackoverflow.com/questions/48641632/extracting-specific-columns-from-pandas-dataframe
import os
import pandas as pd
import numpy as np
from functools import partial

dir_current = os.getcwd()
dir_input = 'input'
filename = 'dataset2.csv'
path_file = os.path.join(dir_current,dir_input,filename)
dataset = pd.read_csv(path_file)
# Periksa jumlah kolom
print('column numbers = %d' % len(dataset.columns)) # 49
dataset = pd.read_csv(path_file,header=None)
df = pd.DataFrame(dataset)
cols = [6,4,13,5,16,17,7,8,8,9,
        10,14,15,11,12,30,31,26,27,18,
        20,21,19,32,33,34,22,23,24,25,
        40,36,42,44,45,46,38,39,37,43,
        41,35,47,48]
df = df[df.columns[cols]]
print('df:\n',df)
print('df.dtypes:\n',df.dtypes)
cat_columns = df.select_dtypes(['object']).columns
print('cat_columns:\n',cat_columns)
for i in cat_columns:
    print(i)
for i in cat_columns:
    df[i] = df[i].astype('category')
df[cat_columns] = df[cat_columns].apply(lambda x: x.cat.codes)
print('df:\n',df)
list_df = df.values.tolist()
print('df (list):\n',list_df)
print('\n',list_df[1-1])
df.to_csv('output2.csv',index=False)

### OUTPUT ###
# D:\Git\learn-py\pandas>python main.py > output.txt
