import pandas as pd
import dask.dataframe as dd
import time

start_time = time.time()
print('\nProgram Started')
df = dd.read_csv('dest_10_6_2.csv', error_bad_lines=False, engine='python', usecols=[28])

# print('Original: ', 'Number of Rows: ', df.shape[0].compute(), 'Number of Columns: ', df.shape[1])

# assign "nan" values to all mixed non-int cells
df['mixed_types'] = dd.to_numeric(df['Amount'], errors='coerce')  # notnull() -> Memory Error

# Drop NA values, listing the converted columns explicitly
#   so NA values in other columns aren't dropped
df = df.dropna(subset=['mixed_types'])

print('After Drop ->', 'Number of Rows:', df.shape[0].compute(), 'Number of Columns: ', df.shape[1])

print('Duration in seconds:', (time.time() - start_time))

# print(df.head())

"""
Memory Error
with open("dest.csv", "r") as f:
    reader = csv.reader(f, delimiter="\t")
    for i, line in enumerate(reader):
        #print('line[{}] = {}'.format(i, line))
        print(i) 
"""

""" Memory Error
start_time = time.time()
with open('dest.csv') as file:
    data = {values[0]: values[1:] for values in zip(*csv.reader(file))}
print("% SECONDS", % (time.time() - start_time))

"""

