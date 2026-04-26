def merge_overlapping_subintervals_brute(arr):
    n=len(arr)
    res=[]
    for i in range(n):
        start=arr[i][0]
        end=arr[i][1]
        if res and end<=res[-1][-1]:
            continue
        for j in range(i+1,n):
            if arr[j][0]<=end:
                end=max(end,arr[j][1])
        res.append([start,end])
    return res


def merge_overlapping_subintervals_optimal(arr):
    n= len(arr)
    arr.sort()
    res=[]
    for i in range(n):
        if res and arr[i][0]<=res[-1][1]:
            res[-1][1]=max(res[-1][1],arr[i][1])
        else:
            res.append(arr[i])
    return res

input_intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_overlapping_subintervals_brute(input_intervals)) 
print(merge_overlapping_subintervals_optimal(input_intervals))
# Time Complexity: O(N^2) for brute force solution, O(N log N) for optimal solution due to sorting.
# Space Complexity: O(N) for both solutions, as we are storing the merged intervals in a new list.