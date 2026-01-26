#Brute force solution - O(nlogn)
def LargestElementBrute(a):
    n=len(a)
    a.sort()
    return a[n-1]

def LargestElementOptimal(a):
    largest=a[0]
    for i in a:
        if i>largest:
            largest=i
    return largest


a=[33,55,22,11,44,29]
print(LargestElementBrute(a))
print(LargestElementOptimal(a))

