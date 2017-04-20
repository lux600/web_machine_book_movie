import numpy as np

# page 47
# arr1 = np.array( [1, 2, 3], float)
# arr2 = np.array( [1, 2, 3], float)
#
# print(arr1 + arr2)  # 더하기
# print(arr1 - arr2)  # 빼기
# print(arr1 * arr2 ) # 곱하기
# print(arr1 / arr2 )  # 나누기
# print(arr1 ** arr2 )  # 제곱

# 48-1
# 배열(행렬)의 크기가 값아야 계산
# arr1 = np.array( [1, 2, 3], float)
# arr2 = np.array( [1, 2], float)
#
# print(arr1 + arr2) # 브로드캐스팅 될 수 없다는 에러 , 작은 차원을 큰 차원에 맞추기 위해, 반복적으로 확장 변환시키는 것

# 48-2
# arr1 = np.array( [ [1,2],[3,4],[5,6] ], float)
# arr2 = np.array( [1,2], float)
# print(arr1)
# print(arr2)
# print(arr1 + arr2)  # arr2 를 계속 나머지도 더해줌 , arr2 가 2차원으로 확장


# 49-1  브로드캐스팅 명시 : newaxis 상수를 이용해서 확장할 축 지정
# arr1 = np.zeros( (2,2), float)
# arr2 = np.array([ 1., 2.], float)
# print(arr1)
# print(arr2)
#
# print("-"*50)
# print(arr1 + arr2)
# print("-"*50)
# print(arr1 + arr2[np.newaxis, :])
# print("-"*50)
# print(arr1 + arr2[:, np.newaxis])

# 49-2 요소를 필터링 하기 위해 불리언 배열 이용
# arr = np.array( [[1,2], [5,9]], float)
# print(arr)
# print(arr >= 7)
# print(arr[arr>=7])
#
# arr = arr[np.logical_and(arr>5 , arr < 11)] # 49-3 배열의 부분 집합
# print(arr)

# 50-1 배열을 인덱스로
# arr1 = np.array([1,4,5,9], float)
# arr2 = np.array( [0,1,1,3,1,1,1], int)
# print(arr1)
# print(arr2)
# print(arr1[arr2])
# print(arr1[[0,1,1,3,1,1,1]])


# 50-2 다차원 배열 연산
# arr1 = np.array([ [1,2],[5,13]], float)
# arr2 = np.array( [1,0,0,1], int)
# arr3 = np.array( [1,1,0,1], int)
#
# print(arr1)
# print("-"*20)
#
# print(arr2)
# print("-"*20)
#
# print(arr3)
# print("-"*20)
#
# print(arr1[arr2, arr3])  # arr2 첫번째 인덱스 배열 , arr3 두번째 인덱스 배열
# print("-"*20)

# 50-3 take 해당 인덱스를 입력받음
# arr1 = np.array( [7,6,6,9], float)
# arr2 = np.array([1,0,1,3,3,1], int)
# arr3 = arr1.take(arr2)
#
# print(arr1)
# print(arr2)
# print(arr3)


# 51-1 take 차원을 명시하여 차원에 따라 부분 집합만 선택
# arr1 = np.array( [ [10,21], [62,33] ] , float)
# arr2 = np.array( [0,0,1], int)
# arr3 = arr1.take(arr2, axis=0)  # 인덱스의 해당 차원별로 선택
# print(arr1)
# print("-"*20)
#
# print(arr2)
# print("-"*20)
#
# print(arr3)


# 51-2  put : take 와 반대
# arr1 = np.array( [2,1,6,2,1,9], float)
# print(arr1)
# print("-"*50)
#
# arr2 = np.array( [3,10,2] , float)
# arr3 = arr1.put([1,4], arr2)
#
#
# print(arr2)
# print("-"*50)
#
# print(arr1) # arr1 이 바뀜


# 51-3 행렬곱( 배열곱)
arr1 = np.array([ [11,22], [23,14]], float)
arr2 = np.array( [ [25,30], [13,33]], float)

print(arr1)
print("-"*50)

print(arr2)
print("-"*50)

print(arr1 * arr2)
