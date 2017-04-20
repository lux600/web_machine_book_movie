import numpy as np
import time

def sum_trad():
    start = time.time()
    X = range(10000000) # 1,000 만개
    Y = range(10000000)
    Z =[]
    for i in range(len(X)):
        Z.append(X[i] + Y[i])

    return time.time() - start

print("time sum =", sum_trad())


def sum_NumPy():
    start = time.time()
    X = np.arange(10000000)
    Y = np.arange(10000000)
    Z = X + Y

    return time.time()-start

print("time sum numpy =", sum_NumPy())