import time
from multiprocessing import Pool

def expensive_calculation(n):
    sum=0
    for i in range(10_000_000):
        sum+=i**2
    return sum*n
if __name__ == '__main__':
    numbers = [1,2,3,4,5,6,7,8]
    start = time.time()
    result = [expensive_calculation(n) for n in numbers]
    print(f"Sequential processing {time.time()-start}")

    start = time.time()
    with Pool(4) as p:
        res=p.map(expensive_calculation,numbers)
    print(f"Parallel processing {time.time()-start}")  

# python3 multiprocessing_python.py 
# Sequential processing 45.08978509902954
# Parallel processing 29.448097944259644