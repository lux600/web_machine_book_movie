import pandas as pd

obj = pd.Series( [3,5,-2,1])
#
print(obj)
print("-"*50)
#
print(obj.values)
print("-"*50)
#
# print(obj.index)
# print(obj.dtype)
# print("-"*50)
#
# Numpy 연산 그대로 적용
print(obj*2)
print("-"*50)

print( obj[obj>2])

# ---------------------------------------

data = { 'a':30, 'b':70, 'c':160, 'd':5}  # 키 값이 인덱스로 생성
obj1 = pd.Series(data)
print(obj1)
#
# print("-"*50)
#
# # 인덱스를 별로의 리스트로 지정 가능
index_num = [ 'a', 'b', 'c', 'd', 'g']
obj2 = pd.Series(data, index= index_num)
print(obj2)  # 해당하는 값이 없으면 NaN  (Not a Number)

print("-"*50)
#
# print(pd.isnull(obj2))  # null 존재 여부
#
# print("-"*50)
#
print(pd.notnull(obj2))  # null 이 아니면 True

# ---------------------------------------

# data = pd.read_csv('ad-dataset/ad.data', header=None)
# print(data)

# print(data.columns)  # 칼럼 갯수

# print(data.dtypes)  # 칼럼 이름의 데이터 타입

# 내용확인
print(data[1].head())  # 2번째 줄의 디폴트로 5개 반환
#
# print("-"*50)
#
# print(data[1].head(10))  # 10개 반환
#
# print("-"*50)
#
# print(data[1].tail())  # 마지막줄부터 2번째, 디폴트로 5개 반환
#
# print("-"*50)
#
# print(data[1:3])

