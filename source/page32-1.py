import pandas as pd
import numpy as np

df = pd.read_csv('ad-dataset/ad.data', header=None)

df = df.replace({'?' : np.nan})
df = df.replace({' ?' : np.nan})
df = df.replace({'  ?' : np.nan})
df = df.replace({'   ?' : np.nan})
df = df.replace({'    ?' : np.nan})
df = df.replace({'     ?' : np.nan})
df = df.fillna(-1)

adindices = df[df.columns[-1]] == 'ad.'
df.loc[adindices, df.columns[-1]] = 1

# print(adindices)


# print("-"*100)
# print(df)

# df.to_csv('ad-dataset/ad-loc.csv')

nonadindices = df[df.columns[-1]] == 'nonad.'
df.loc[nonadindices, df.columns[-1]] = 0

# df.to_csv('ad-dataset/ad-loc2.csv')

df[df.columns[-1]] = df[df.columns[-1]].astype(float)
df.apply(lambda x : pd.to_numeric(x))


print("-"*100)
print(df)

# df.to_csv('ad-dataset/ad-apply.csv')
