import math
def check(m,n):
    for i in range(m, n+1):
        if i < 2:
            continue

        is_prime = True                           # Bug 4 fixed: reset per number

        for j in range(2, int(math.sqrt(i)) + 1):# Bug 3 fixed: int cast
            if i % j == 0:
                is_prime = False                  # Bug 5 fixed: consistent variable
                break

        if is_prime and '3' not in str(i):        # Bug 2 fixed: inside loop
                print(i, end=' ')                     # Bug 6 fixed: digit filter added

m=3
n=20
check(m,n)