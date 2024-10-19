# U (Understanding):
#     - We are given the head of a singly linked list and need to determine if there is a cycle in it.
#     - A cycle occurs if a node's `next` pointer points to one of the previous nodes in the list, forming a loop.
#     - If there is no cycle, the list ends with a `None` reference.
#     - Input: The head of a linked list (could be None or a non-empty list).
#     - Output: Return `True` if there is a cycle; otherwise, return `False`.

# M (Methods):
#     - We will use the **Tortoise and Hare** (Floyd's Cycle Detection) method.
#     - This involves two pointers:
#         - The `slow` pointer moves one step at a time.
#         - The `fast` pointer moves two steps at a time.
#     - If there is a cycle, these two pointers will eventually meet at some point in the cycle.
#     - If there is no cycle, the `fast` pointer will reach the end of the list (None).

# P (Plan):
#     - Start both `slow` and `fast` at the `head` of the list.
#     - Move `slow` one step at a time and `fast` two steps at a time in the loop.
#     - If `fast` reaches the end of the list (i.e., `fast == None` or `fast.next == None`), there is no cycle, so return `False`.
#     - If at any point `slow == fast`, it means a cycle exists, and we return `True`.

# I (Implementation):

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers, both starting at the head of the list
        fast = slow = head
        
        # Loop to move fast and slow pointers through the list
        while fast and fast.next:  # Check if fast and fast.next are not None
            # Move the slow pointer one step
            slow = slow.next
            
            # Move the fast pointer two steps
            fast = fast.next.next
            
            # If the slow pointer and fast pointer meet, there is a cycle
            if slow == fast:
                return True
        
        # If the loop terminates, it means there is no cycle
        return False

# R (Results):
#     - Example 1: Given a list with a cycle, the function returns `True`.
#     - Example 2: Given a list with no cycle, the function returns `False`.
#     - Example 3: If the list is empty (None), return `False` since there's no cycle.

# E (Efficiency):
#     - Time Complexity: O(n), where n is the number of nodes in the list. We traverse each node at most once.
#     - Space Complexity: O(1), since we are using only two pointers (`fast` and `slow`), regardless of the list size.
