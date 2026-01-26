# Time Complexity: O(N), where N is the size of the array. This is because we traverse the array once to shift the elements.

# Space Complexity: O(N), as we are using a temporary array of the same size as the input array to store the shifted elements.

def LeftRotateByOnePlaceBrute(a):
    n=len(a)
    temp=[0]*n
    for i in range(1,n):
        temp[i-1]=a[i]
    temp[n-1]=a[0]
    return temp

def LeftRotateByOnePlaceOptimal(a):
    temp=a[0]
    n=len(a)
    for i in range(1,n):
        a[i-1]=a[i]
    a[n-1]=temp
    return a
a=[3,5,7,9,4,6,8]
print(LeftRotateByOnePlaceBrute(a))
print(LeftRotateByOnePlaceOptimal(a))