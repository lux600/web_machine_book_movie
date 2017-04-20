import numpy as np

# arr = np.array( [ 2. , 6. , 5. , 5.])
# print(arr)
# print("*"*100)

# print("\n")
# print(arr[:3])
#
# print("\n")
# print(arr[3])
#
# print("\n")
# arr[0] = 5
# print(arr)

# -----------------------------------------------

# # 41-1 : unique()  중복 제거
# arr1 = np.unique(arr)
# print(arr1)
#
# # 41-2 : 정렬
# arr1 = np.sort(arr)
# print(arr1)
#
# # 41-3 : 정렬한 후,  인덱스 순서 변경
# arr1 = np.argsort(arr)
# print(arr1)
#
# # 41-4 무작위 재배열
# arr1 = np.random.shuffle(arr)
# print(arr)
#
# # 41-5 배열을 비교
# arr1 = np.array_equal(arr, np.array( [1,3,2]))
# print(arr1)


# -----------------------------------------------

# # 41-6
# matrix = np.array(   [ [4., 5., 6.],[2, 3, 6]], float)
# print(matrix)
# print(matrix[0,0])  # 1 x 1 번째
# print(matrix[0,2])

# -----------------------------------------------

# 42-1 슬라이싱 : 잘라낼 시작부분 인덱스 : 끝 인덱스
# arr = np.array(   [ [4., 5., 6.],[2., 3., 7.]], float)
# print(arr)
# arr1 = arr[1:2, 2:3]
# print(arr1)

# 42-2
# arr = np.array(   [ [4., 5., 6.],[2., 3., 7.]], float)
#
# print(arr)
# print( arr[1, : ])  # 1 +1 행
# print( arr[:, 2])   # 1 +2 열
# print( arr[-1: , -2:])  # 행의 -1(마지막) 모두 =>  열의 -2(마지막2번쨰) 에서 오른쪽

# 42-3
# arr = np.array( [[ 10,29,23],[24,25,46]], float)
#
# print(arr)
# arr1 = arr.flatten() # 다차원 배열을 1차원 배열로 변경
# print(arr1)
#
# print(arr.shape)  # 배열 크기
# print(arr.dtype)  # 배열에 저장된 값의 타입

# 43-1
# matrix = np.array(   [ [4., 5., 6.],[2, 3, 6]], float)
# int_arr = matrix.astype(np.int32)  # 타입변환
# print(int_arr)
# print(int_arr.dtype)

# 43-2
# arr = np.array(   [ [4., 5., 6.],[2, 3, 6] ], float)
# print(arr)
# print( len(arr) )  # 첫번째 차원의 길이 반환
# print( 2 in arr )  # 배열요소 해당값 존재하는지


# 43-3
# 배열의 요소를 다른 차원으료 변경
# arr = np.array( range(8), float)
# print(arr)
#
# arr = arr.reshape( (4,2)) # 배열 차원 변경
# print(arr)
# print(arr.shape)  # 배열 행,열 크기

# 44-1
# arr = np.array(range(6), float).reshape( (2,3) )
# print(arr)
#
# print(arr.transpose())  # 전치 행렬로 변환

# 44-2
# matrix =np.arange(15).reshape((3,5))
# print(matrix)
# print(matrix.T)  # 전치 행렬

# 45-1 : newaxis 상수로 차원 늘리기
# arr = np.array([14,32,13], float)
# print(arr)
# arr1 = arr[:, np.newaxis]# 차원 늘리기
# print(arr1)
# print(arr1.shape)
#
# arr2 = arr[ np.newaxis, :]
# print(arr2)
# print(arr2.shape)

# 45-2 : concatenate() 결합
# arr1 = np.array( [10,22], float)
# arr2 = np.array( [31,43,54,61], float)
# arr3 = np.array( [71,822,29], float)
#
# arr = np.concatenate( (arr1, arr2, arr3))  # 1차원 배열만  결합하는 경우
# print(arr)

# 45-3 다차원 배열 결합 , 디폴트는 첫번째 차원
# arr1 = np.array( [ [11,12],[32,42] ], float)
# arr2 = np.array([ [54,26], [27,28] ], float)
# arr = np.concatenate( (arr1, arr2) )
# print(arr)
#
# arr1_1 = np.concatenate( (arr1, arr2), axis=0 )
# print(arr1_1)
#
# arr1_2 = np.concatenate( (arr1, arr2), axis=1 ) # 각각 번째의 행 끼리 결합
# print(arr1_2)



# 46-1  바이너리 형태로 저장 및 복원
arr = np.array( [10, 20, 30], float)
print(arr)
str = arr.tostring()   # 바이너리 형태
print(str)

to = np.fromstring(str) # 다시 복원
print(to)
