import numpy as np


# 37-2 같은값으로 채우기 fill
# arr = np.array( [10, 20, 33], float)
# print("arr=", arr)
#
# arr.fill(1)
# print("arr=", arr)

# 37-3 배열을 램덤하게 생성 : random 서브 모듈
# arr = np.random.permutation(5)
# print("arr=", arr)

# print("-"*50)
# 37-4 정규분포를 따르는 함수 normal  0 : 평균, 1 : 표준편차, 5 : 배열 요소 갯수
# arr = np.random.normal(0 , 1, 5)
# print("arr=", arr)


# 38-1 random 함수는 균등분포 , 0~1 사이의 값을 반환 , 0,1 은 포함되지 않음
# arr = np.random.random(5)
# print("arr=",arr)


# 38-2 identity() : 2차원 배열(행렬)의 단위행렬 생성함수
# arr = np.identity( 5, dtype=float)
# print(arr)


# 38-3 eye() 함수는 k번째 대각 1인 행렬
# 주대각 0, k 번째의 대각선 행렬, 양수는 상대각, 음수는 하대각
# arr = np.eye(5, k=-1 , dtype=float)
# print(arr)


# 38-4 행과 열 을 1 로 채움
# arr = np.ones( (2,3) , dtype=float )
# print(arr)
#
# print("\n\n")
# # 38-5 해당하는 열을 0으로 채움
# arr = np.zeros( 6, dtype=int)
# print(arr)


# 39-1
arr = np.array([ [13, 32, 31],  [64, 25, 76] ], float)
print(arr)
#
# print("\n"*2)
#
# # 0 으로 채움
# arr0 = np.zeros_like(arr)
# print(arr0)
#
# print("\n"*2)
#
# # 1로 채움
# arr1 = np.ones_like(arr)
# print(arr1)


# 39-2 random() 서브모듈
# random.rnad : 0, 1 사이의 균등분포 2 x 3 의 행렬
# arr = np.random.rand(2, 3)
# print(arr)

# 39-3
# # random.mutlivariate_normal() : [10,0] 평균벡터,  [ [3,1], [1,4] ], 공분산 행렬  size=[5,]생성될 샘플 갯수
arr = np.random.multivariate_normal( [10,0], [ [3,1], [1,4] ], size=[5,])
print(arr)