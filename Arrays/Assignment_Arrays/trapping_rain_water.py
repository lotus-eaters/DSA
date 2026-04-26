def trap(self, height: List[int]) -> int:
    n = len(height)
    lb=[0]*n
    rb=[0]*n
    potentialHeight=0
    maxWaterTrapped=0
    lb[0]=height[0]
    for i in range(1,n):
        lb[i] = max(lb[i-1],height[i])
    rb[n-1]=height[n-1]
    for i in range(n-2,-1,-1):
        rb[i] = max(rb[i+1],height[i])
    for i in range(n):
        potentialHeight=min(lb[i],rb[i])
        maxWaterTrapped += potentialHeight - height[i] 
    return maxWaterTrapped

height =[0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))  # Output: 6