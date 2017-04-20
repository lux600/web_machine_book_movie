import pandas as pd
import numpy as np
import random

data = pd.read_csv('ad-dataset/ad.data', header=None)

# obj1 = data[data[1] > 0 ].head(4)  # str() > int() 에러
# print( obj1  )

# print(data[1].values)


# 특징이 1이 0보다 크고, 광고를 포함하는 웹페이지 선택
# print (  data[  (data[1]>0) & (data[1558]=='ad.')].head(4)    )

# 인덱스를 지정한 행 선택
# print(  data.ix[:3]  )
# ix ( 0부터 시작해서 레이블이 3이 나타날 때까지 선택)
# iloc ( 0에서 3열까지 선택)

# print(  data.loc[:3]  ) # loc 는 3행 레이블까지 포함

#page 64 ------------------------------------------------------
# ==>칼럼 전체를 하나의 값으로 설정
#print(data[1547])
# data[1547]= 0
# print( data[1547] )


# ==> 특정셀을 원하는 값으로 설정
# print( data.ix[3,1])
#
# data.ix[3,1] =0
# print( data.ix[3,1])

# ==> 전체 행을 값의 집합으로 지정
#import random

# print( data.ix[0] )

# print (random.randint(0,1))

# data.ix[0] = [ random.randint(0,1) for r in range(1558)] + ['ad.']  # xrange -> range
# print(data.ix[0])

# new_list = []
# for i in old_list :
#   if filter(i):
#       new_list.append(expressions(i))

# ++> new_list = [ expression(i) for i in old_list if filter(i) ]

# new_list = []
# for i in range(1558):
#   new_list.append( random.randint(0,1) )
# new_list.append('ad.')


# ==> 배열을 Series 객체로 변환해 DataFrame 의 마지막 행을 추가
#row = [ random.randint(0,1) for r in range(1558)] + ['ad.']

# print(row)
#print(data.columns)
#print("-"*50)

#print(data)

#print("-"*50)

# Series : 키 와 value 설정
# data = data.append( pd.Series(row, index= data.columns), ignore_index=True)
# print(data)

# ==> append 함수 대신 loc 함수로 마지막 라인에 행을 추가
# print(len(data))
# data.loc[ len(data )] = row

#page 65 ------------------------------------------------------

# ==>drop 함수로 칼럼을 지움
# data['newcolumn'] = 'test value'
# print(data)
#
# print("-"*50)
#
# data = data.drop("newcolumn", 1)
# print(data.columns)
# print("-"*50)
# print(data)


# ==> 각 행의 중복 여부를 체크
# print(data.duplicated())  # 14번째가 2번째와 중복

#==> drop_duplicates 유일한 값으로 구성된 DataFrame 을 반환
# print( data[1558].drop_duplicates())
#
# print("-"*50)
# #===> 반환 결과를 리스트로 저장
# print( data[1558].drop_duplicates().tolist() )
#
# # 데이터타입은 여전히 object 타입
# print(data[1558].dtypes)

# ==> float 로 변환
# print(data.columns[-1])
# print(data[data.columns[-1]])
# data[data.columns[-1]] = data[data.columns[-1]].astype(float)  # error

# 문자열과 섞인 부분을 숫자로 바꾸는 작업
data= data.replace({'?': np.nan})
data= data.replace({' ?': np.nan})
data= data.replace({'  ?': np.nan})
data= data.replace({'   ?': np.nan})
data= data.replace({'    ?': np.nan})
data= data.replace({'     ?': np.nan})
data= data.replace({'      ?': np.nan})  # 물음표를 np.nan 로 바꿈

# 누락 데이터가 포함된 행을 제거하는 방법
# data = data.dropna()  # 10번째 삭제
# print(data)

# 빈 셀에 상수로 채움
data = data.fillna(-1)  # -1 로 채움
# print(data)

# DataFrame 의 각 칼럼을 숫자 타입으로 바꿔주는 lambda 함수를 적용
# apply() 함수는 특정 축을 따라 함수를 적용한다 , 디폴트는 index 축이다
# 인덱스 x 는 칼럼, to_numeric 함수는 x를 가장 비슷한 숫자 타입으로 바꿈 ( 여기에서는 float 가 됨 )
#data = data.apply( lambda x : pd.to_numeric(x) )  # ad 에러남

data1 = pd.DataFrame(columns= [i for i in range(1559)])
print(data1)
print("-"*50)

print( "len(data1)=",len(data1) )
print("-"*50)

# 마지막 행에 1개 추가
data1.loc[ len(data1) ] = [ random.randint(0,1) for r in range(1558)] + [1]  # 랜덤하게 입력후 + 마지막 1 추가
print(data1)
print("-"*50)

data1.loc[ len(data1) ] = [ random.randint(0,1) for r in range(1558)] + [1]  # 랜덤하게 입력후 + 마지막 1 추가

print("-"*50)
print( len(data) )

# 원래의 테이블 data 와 concat() 함수를 통해 병합되면서, data 의 아래로 data1 의 행이 붙는다
dataot = pd.concat( [data[:], data1[:]] )   # 2개 추가됨
print( len(dataot) )




