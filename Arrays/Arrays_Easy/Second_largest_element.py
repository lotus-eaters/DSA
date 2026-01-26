def secondLargestBrute(a):
    n=len(a)
    a.sort()
    return a[n-2]
#O(nlogn)

#Two pass solution 1 pass is to find largest, the other is to find secondLargest - O(2n)
def secondLargestBetter(a):
    n=len(a)
    if n<2:
        return None
    largest=-1
    for num in a:
        if num>largest:
            largest=num
    secondLargest=-1
    found=False
    for num in a:
        if num!=largest and num>secondLargest:
            secondLargest=num
            found=True
    if not found:
        return None
    return secondLargest

#Single pass - O(n)
def secondLargestOptimal(a):
    largest=smallest=float('-inf')
    for num in a:
        if num>largest:
            second=largest
            largest=num
        elif num!=largest and num>second:
            second=num
    return second

a=[5,10,7,4,2,1]
print(secondLargestBrute(a))
print(secondLargestBetter(a))
print(secondLargestOptimal(a))
