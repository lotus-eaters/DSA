import time
from functools import lru_cache

def factorial_slow(n):
    return 1 if n==0 else n*factorial_slow(n-1)

@lru_cache(maxsize=0)
def factorial_fast(n):
    return 1 if n==0 else n*factorial_fast(n-1)

start=time.time()
for i in range(100):
    factorial_slow(i)
print(f"Without Cache {time.time()-start}")

start=time.time()
for i in range(100):
    factorial_fast(i)
print(f"With Cache {time.time()-start}")

