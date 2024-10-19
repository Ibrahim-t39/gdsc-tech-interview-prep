# U (Understanding):
#     - What is the maximum input size? 
#         - Large input sizes are allowed, typically up to 10^4 or 10^5 elements.
#     - What will the return data type be? 
#         - A list of two indices where the values at those indices sum up to the target (e.g., [0,1]).
#     - Can we have an empty list as input?
#         - Yes, but we should return nothing in this case since no pairs can exist.
#     - If the list contains only one element, what should be returned?
#         - If the list has less than two elements, no valid pair exists, so return nothing.
#     - What if none of the elements sum up to the target?
#         - If no pair is found, return nothing or an empty list.

# M (Methods):
#     - Brute-force approach using nested loops (O(n^2)).
#     - Optimized approach using a hashmap to store already seen elements (O(n)).

# P (Plan):
#     - Brute-force method would iterate over every possible pair (i, j), which results in O(n^2) time complexity.
#     - The optimized approach:
#         - We use a hashmap (dictionary) to store the values we’ve seen so far.
#         - For each element in the list, we check if `target - current_element` exists in the hashmap.
#         - If found, return the indices of these two elements.
#         - Otherwise, add the current element and its index to the hashmap.

# I (Implementation):
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store the value and index of each element we've seen
        nums_dict = {}
        
        # Loop through each element in the list, using both index and value
        for index, num in enumerate(nums):
            # Calculate the complement (difference) we need to find
            difference = target - num
            
            # If the complement exists in the dictionary, return its index and the current index
            if difference in nums_dict:
                return [nums_dict[difference], index]
            
            # Otherwise, store the current number with its index in the dictionary
            nums_dict[num] = index

# R (Results):
#     - Example 1: nums = [2, 7, 11, 15], target = 9:
#         - First iteration: difference = 9 - 2 = 7, 7 is not in nums_dict, add 2 with its index (0).
#         - Second iteration: difference = 9 - 7 = 2, 2 is in nums_dict, so return [0, 1].
#     - Example 2: nums = [3, 2, 4], target = 6:
#         - First iteration: difference = 6 - 3 = 3, 3 is not in nums_dict, add 3 with its index (0).
#         - Second iteration: difference = 6 - 2 = 4, 4 is not in nums_dict, add 2 with its index (1).
#         - Third iteration: difference = 6 - 4 = 2, 2 is in nums_dict, so return [1, 2].
#     - Example 3: nums = [3, 3], target = 6:
#         - First iteration: difference = 6 - 3 = 3, 3 is not in nums_dict, add 3 with its index (0).
#         - Second iteration: difference = 6 - 3 = 3, 3 is in nums_dict, so return [0, 1].

# E (Efficiency):
#     - Time Complexity: O(n), where n is the number of elements in the list. We loop through the list once.
#     - Space Complexity: O(n), for storing the dictionary in the worst case, when no pairs are found and all elements are stored.
