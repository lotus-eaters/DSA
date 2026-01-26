def checksortedarray(a):
    n=len(a)
    sorted=True
    for i in range(n-1):
        if a[i]>a[i+1]:
            sorted=False
            break
    return sorted
a=[6,4,2,3,4,5]
print(checksortedarray(a))
a1=[3,4,5,6]
print(checksortedarray(a1))

