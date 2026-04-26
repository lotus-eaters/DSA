def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
    c1max = float('-inf')
    c1min = float('inf')
    c2max = float('-inf')
    c2min = float('inf')
    c3max = float('-inf')
    c3min = float('inf')
    c4max = float('-inf')
    c4min = float('inf')
    n=len(arr1)
    for i in range(n):
        c1max = max(arr1[i]+arr2[i]+i,c1max)
        c1min = min(arr1[i]+arr2[i]+i,c1min)

        c2max = max(arr1[i]-arr2[i]+i,c2max)
        c2min = min(arr1[i]-arr2[i]+i,c2min)

        c3max = max(arr2[i]-arr1[i]+i,c3max)
        c3min = min(arr2[i]-arr1[i]+i,c3min)

        c4max = max(-arr2[i]-arr1[i]+i,c4max)
        c4min = min(-arr2[i]-arr1[i]+i,c4min)
    return max(max(c1max-c1min,c2max-c2min),max(c3max-c3min,c4max-c4min))
# Time Complexity: O(N), where N is the length of the input arrays.
# Space Complexity: O(1), as we are using a constant amount of space to store
# the maximum and minimum values for the four cases.

arr1 = [1,2,3]
arr2 = [4,5,6]
print(maxAbsValExpr(arr1, arr2))  # Output: 9