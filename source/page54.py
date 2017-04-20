import numpy as np

arr = np.random.rand(8,4)  # 0~1 균등분포 8 x 4 행렬
print(arr)
print("-"*50)

print(arr.mean())  # 평균
print(np.mean(arr))
print("-"*50)

print(arr.sum())
print(np.sum(arr))