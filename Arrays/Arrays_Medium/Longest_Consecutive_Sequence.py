def longest_consecutive_seq_brute_force(nums):
    if not nums:
        return 0

    longest_streak = 1

    for num in nums:
        current_num = num
        current_streak = 1

        while current_num + 1 in nums:
            current_num += 1
            current_streak += 1

        longest_streak = max(longest_streak, current_streak)

    return longest_streak

def longest_consecutive_seq_optimal(nums):
    if not nums:
        return 0

    num_set = set(nums)
    longest_streak = 1

    for num in num_set:
        if num - 1 not in num_set:  # Check if it's the start of a sequence
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak
#time complexity: O(N) for optimal solution, O(N^2) for brute force solution
#space complexity: O(N) for optimal solution, O(1) for brute force solution
a = [100, 4, 200, 1, 3, 2] 
print(longest_consecutive_seq_brute_force(a))  # Output: 4 (sequence is [1, 2, 3, 4])
print(longest_consecutive_seq_optimal(a))      # Output: 4 (sequence is