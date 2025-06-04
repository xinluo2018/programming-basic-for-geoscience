from multiprocessing import Pool
import time 
import sys

def task(x):
    return x * x

# if __name__ == '__main__':
with Pool(4) as pool:  # 4个工作进程
    result = pool.map(task, range(10))  # 并行map
print(result)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



