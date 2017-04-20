import pandas as pd
import numpy as np
from sklearn.svm import SVC

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


dataset = df.values[:,:]
np.random.shuffle(dataset)

data = dataset[:,:-1]
labels = dataset[:,-1].astype(float)

ntrainrows = int(len(data)*.8)

train = data[:ntrainrows, :]
trainlabels = labels[:ntrainrows]
test = data[ntrainrows:, :]
testlabels = labels[ntrainrows:]

#---------------------------------------------------

clf = SVC(gamma=0.001, C=100.)  # SVC 모델 선언
clf.fit(train, trainlabels)   # fit 함수를 호출해 훈련 데이터로 모델을 훈련 (3장 )

score = clf.score(test, testlabels)  # 20% 테스트 케이스를 예측할 때의 평균 정확도는 score 함수 사용
print('score=', score)



