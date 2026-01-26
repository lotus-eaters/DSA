def linear_search(nums,key):
    found=False
    for i in range(len(nums)):
        if nums[i]==key:
            found=True
            break
    if found:
        return print(f'{nums[i]} is found at index {i}')
    else:
        return print(f'{nums[i]} is not found')
        
nums=[24,46,68,97,75,53,31]
key=75
linear_search(nums,key)