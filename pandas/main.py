# https://chrisalbon.com/python/data_wrangling/pandas_dataframe_importing_csv/
# https://stackoverflow.com/questions/32011359/convert-categorical-data-in-pandas-dataframe
import os
import pandas as pd
import numpy as np
from functools import partial

dir_current = os.getcwd()
dir_input = 'input'
filename = 'dataset.csv'
path_file = os.path.join(dir_current,dir_input,filename)
dataset = pd.read_csv(path_file)
# Periksa jumlah kolom
print('column numbers = %d' % len(dataset.columns)) # 44
id_col = 0 # Index column
df = pd.read_csv(path_file,index_col=id_col)
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
df.to_csv('output.csv',index=False)

### OUTPUT ###
# D:\Git\learn-py\pandas>python main.py > output.txt
