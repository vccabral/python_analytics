

print("this the pandas library")
print("http://pandas.pydata.org/")
print("pip install pandas")

import pandas as pd

df = pd.read_csv('example09.csv', header=None)

for row in df.iterrows():
	print(row)

for row in df.itertuples():
	print(row)

df.to_csv('exmaple09-out.csv')