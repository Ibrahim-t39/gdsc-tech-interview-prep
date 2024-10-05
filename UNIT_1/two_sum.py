# U (Understanding):
#     - What is the maximum input size?
#     - What will the return data type be? (e.g., [0,1] if target found)?
#     - Can we have an empty list as input?
#     - If the list contains only one element, what should be returned?
#     - What if none of the elements sum up to the target?

# M (Methods):
#     - Hashmap/Dictionary
#     - List

# P (Plan):
#     - Fun fact: n-sum has time complexity O(n^(n-1))
    
#     - Brute force approach:
#         - One loop that iterates through the list with index `i`.
#         - Nested loop `j` iterates again to check if `nums[i] + nums[j] == target`.
#         - Example: nums = [2, 7, 11, 15], target = 9 (O(n^2))
#             - i, j pair checks

#     - Optimized approach:
#         - Example: nums = [(0, 2), (1, 7), (2, 11), (3, 15)]
#         - Initialize an empty dictionary `nums_dict`.
#         - Loop through the enumerated list `nums`.
#         - Initialize a variable `difference = target - num`.
#         - If `difference` is in `nums_dict`, return the index of `difference` and the current index.
#         - Otherwise, add `num` and its index to the dictionary.

# I (Implementation):

nums_dict = {}

for index, num in enumerate(nums):
    difference = target - num
    if difference in nums_dict:
        return [nums_dict[difference], index]
    else:
        nums_dict[num] = index

# R (Results):
#     - For nums = [2, 7, 11, 15] and target = 9:
#         - On the first iteration, difference = 9 - 2 = 7, which is not in nums_dict, so 2 is added to the dictionary.
#         - On the second iteration, difference = 9 - 7 = 2, and since 2 is in the dictionary, the algorithm returns [0, 1].
#     - Final output: [0, 1], meaning nums[0] + nums[1] = 9.

# E (Efficiency):
#     - Time Complexity:
#         - Optimized approach: O(n) because we iterate through the list once.
#         - Brute force approach: O(n^2) because of the nested loops.
#     - Space Complexity: O(n) in the worst case, where all elements are added to the dictionary.
