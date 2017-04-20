import pandas as pd
import numpy as np

df = pd.read_csv('ad-dataset/ad.data', header=None)

# df.to_csv('ad-dataset/ad_data.csv')

print("np.nan=", np.nan)
print("type(df)=", type(df))

# print(df)
#
df = df.replace({'?' : np.nan})
df = df.replace({' ?' : np.nan})
df = df.replace({'  ?' : np.nan})
df = df.replace({'   ?' : np.nan})
df = df.replace({'    ?' : np.nan})
df = df.replace({'     ?' : np.nan})
# print(df)
df = df.fillna(-1)
#
# print("-"*100)
# print(df)

# df.to_csv('ad-dataset/ad-result.csv')

