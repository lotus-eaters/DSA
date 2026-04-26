def merge_two_sorted_Arrays_brute(a1, a2):
    n=len(a1) 
    m=len(a2)
    a3=[0]*(n+m) 
    left=0
    right=0
    index=0
    while left<n and right<m:
        if a1[left]<=a2[right]:
            a3[index]=a1[left]
            left+=1
            index+=1
        else:
            a3[index]=a2[right]
            right+=1
            index+=1
    while left<n:
        a3[index]=a1[left]
        left+=1
        index+=1
    while right<m:
        a3[index]=a2[right]
        right+=1
        index+=1
    for i in range(n+m):
        if i<n:
            a1[i]=a3[i]
        else:
            a2[i-n]=a3[i]
    return a1,a2

def merge_two_sorted_Arrays_optimal(a1, a2):
    n=len(a1) 
    left = n-1 
    right=0
    while left>=0 and right<len(a2):
        if a1[left]>a2[right]:
            a1[left],a2[right]=a2[right],a1[left]
            left-=1
            right+=1
        else:
            left-=1
    a1=sorted(a1)
    a2=sorted(a2)
    return a1,a2

def merge_two_sorted_arrays_optimal2(a1,a2):
    n=len(a1)
    m=len(a2)
    length=n+m
    gap = length//2 + length%2
    while gap>0:
        left=0
        right=left+gap
        while right<length:
            if left<n and right>=n:
                if a1[left]>a2[right-n]:
                    a1[left],a2[right-n]=a2[right-n],a1[left]
            elif left>=n:
                if a2[left-n]>a2[right-n]:
                    a2[left-n],a2[right-n]=a2[right-n],a2[left-n]
            else:
                if a1[left]>a1[right]:
                    a1[left],a1[right]=a1[right],a1[left]       
            left+=1
            right+=1
        if gap==1:
            break
        else:
            gap=gap//2 + gap%2
    return a1,a2

def merge_two_sorted_arrays_optimal3_singlearray(a1,a2,m,n):
    left1=m-1
    left2=n-1
    pos=m+n-1
    while left2>=0 and left1>=0:
        if left1>=0 and a1[left1]>=a2[left2]:
            a1[pos]=a1[left1]
            left1-=1
        else:
            a1[pos]=a2[left2]
            left2-=1
        pos-=1
    return a1

a1=[1,3,5,7]
a2=[2,4,6,8]
print(merge_two_sorted_Arrays_brute(a1,a2))  # Output: ([1, 2, 3, 4], [5, 6, 7, 8])
print(merge_two_sorted_Arrays_optimal(a1,a2))  # Output: ([1, 2, 3, 4], [5, 6, 7, 8])
print(merge_two_sorted_arrays_optimal2(a1,a2))  # Output: ([1, 2, 3, 4], [5, 6, 7, 8])
n1=[1,2,3,4,0,0,0,0] 
m=4
n=4
n2=[5, 6, 7, 8]
print(merge_two_sorted_arrays_optimal3_singlearray(n1,n2,m,n))  # Output: ([1, 2, 3, 4], [5, 6, 7, 8])
# Time Complexity: O(N+M) for brute force and optimal solutions, O((N+M) log(N+M)) for the second optimal solution due to sorting.
# Space Complexity: O(N+M) for brute force solution, O(1) for optimal solutions as we are merging in place.     

