
import pandas as pd
filename = 'dest_10_6_4.txt'

result = []
# Memory Error
chunksize = 10 ** 6
for chunk in pd.read_csv(filename, chunksize=chunksize, error_bad_lines=False, engine='python', usecols=[28]):
    chunk['mixed_types'] = chunk.to_numeric(chunk['Amount'], errors='coerce')
    chunk = chunk.dropna(subset=['mixed_types'])
    # result.append(sum(chunk['Amount']))
    # print('Number of Rows: ', chunk.shape[0], 'Number of Columns: ', chunk.shape[1])
#  = sum(result)
# print('TOTAL:', total)
print('End of Code!')
# chunks = pd.read_csv(filename, chunksize=100000,  engine='python')
# print('Number of Rows: ', chunks.shape[0], 'Number of Columns: ', chunks.shape[1])
# data = pd.concat(chunks)

"""
Memory Error
LARGE_FILE = 'dest.csv' 
CHUNKSIZE = 100000  # processing 100,000 rows at a time


def process_frame(df):
    # process data frame
    return len(df)


reader = pd.read_csv(LARGE_FILE, chunksize=CHUNKSIZE, error_bad_lines=False,  engine='python')
result = 0
for df in reader:
    # process each data frame
    result += process_frame(df)

print('There are %d rows of data' % result)
"""