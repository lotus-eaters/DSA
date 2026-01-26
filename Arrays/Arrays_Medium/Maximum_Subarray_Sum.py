def max_subarray_sum_brute(nums):
    n=len(nums)
    maxi=0
    for i in range(n):
        for j in range(i,n):
            sum=0
            for k in range(i,j):
                sum+=nums[k]
            maxi=max(maxi,sum)
    return maxi

def max_subarray_sum_better(nums):
    n=len(nums)
    maxi=-999
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=nums[j]
            maxi=max(sum,maxi)
    return maxi

def max_subarray_sum_optimal(nums):
    n=len(nums)
    maxi=0
    sum=0
    for i in range(n):
        sum+=nums[i]
        if sum>maxi:
            maxi=max(sum,maxi)
        if sum<0:
            sum=0
    return maxi

def max_subarray_sum_optimal_printsubarray(nums):
    n=len(nums)
    maxi=0
    sum=0
    for i in range(n):
        if sum==0:
            start=i
        sum+=nums[i]
        if sum>maxi:
            startindex=start 
            endindex=i
            maxi=max(sum,maxi)
        if sum<0:
            sum=0
    for i in range(startindex,endindex):
        print(nums[i]," ")
    # return maxi

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum_brute(arr))
print(max_subarray_sum_better(arr))
print(max_subarray_sum_optimal(arr))
print(max_subarray_sum_optimal_printsubarray(arr))
