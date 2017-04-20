import numpy as np

# 52-1
X = np.arange(15).reshape((3,5))
print(X)
#
# print("-"*50)
# print(X.T)
#
# print("-"*50)
# print( np.dot(X.T, X))   # X^T X 내적

# 52-2
# arr1 = np.array( [12,43,10], float)
# arr2 = np.array( [21,42,14], float)
#
# print( np.outer(arr1, arr2))
# print("-"*50)
#
# print(np.inner(arr1, arr2))
# print("-"*50)
#
# print(np.cross(arr1, arr2))


# 53-1
matrix = np.array( [ [74,22,10], [92,31,17], [21,22,12]], float)
print(matrix)
print("-"*50)

print(np.linalg.det(matrix))  # determinant
print("-"*50)

inv_matrix = np.linalg.inv(matrix) # 역행렬
print(inv_matrix)
print("-"*50)

vals , vecs = np.linalg.eig(matrix)  # 고유값, 고유벡터
print(vals)
print("-"*50)
print(vecs)