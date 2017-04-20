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
nonadindices = df[df.columns[-1]] == 'nonad.'
df.loc[nonadindices, df.columns[-1]] = 0

df[df.columns[-1]] = df[df.columns[-1]].astype(float)
df.apply(lambda x : pd.to_numeric(x))

# ------------------------------------------------------

dataset = df.values[ : , : ]
np.random.shuffle(dataset)

data = dataset[:,:-1]
labels = dataset[:,-1].astype(float)

total = int(len(data))
ntrainrows = int(len(data)*.8)

print("ntrainrows=",ntrainrows, " total=",total)

print(labels)

train = data[:ntrainrows, :]
trainlabels = labels[:ntrainrows]

test = data[ntrainrows:, :]
testlabels = labels[ntrainrows:]
