# U (Understanding):
#     - Input: A singly linked list.
#     - Output: A singly linked list where all nodes are reversed.
#     - Edge cases:
#         - If the input list is empty (`head` is None), return None.
#         - If the input list contains only one node, the reversed list is the same as the input list.

# M (Methods):
#     - Use an iterative approach to reverse the linked list by updating the pointers.
#     - We will maintain three pointers:
#         - `prev`: Tracks the previous node (initially None).
#         - `current`: Tracks the current node we're processing.
#         - `next_node`: Temporarily stores the next node before we reverse the `current.next` pointer.

# P (Plan):
#     - Initialize `prev` to None (since the reversed list's last node will point to None).
#     - Set `current` to the head of the original list.
#     - Loop until `current` becomes None:
#         - Temporarily store the next node in `next_node`.
#         - Reverse the pointer of the current node (`current.next = prev`).
#         - Move `prev` and `current` one step forward (`prev = current`, `current = next_node`).
#     - When the loop ends, `prev` will be pointing to the new head of the reversed list.
#     - Return `prev`.

# I (Implementation):

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the list is empty, return None
        if not head:
            return None
        
        # Initialize previous pointer to None, current pointer to head
        prev = None
        current = head
        
        # Iterate through the list and reverse the pointers
        while current:
            # Save the next node before reversing
            next_node = current.next
            
            # Reverse the current node's pointer
            current.next = prev
            
            # Move pointers one step forward
            prev = current
            current = next_node
        
        # Return the new head, which is the previous node after the loop ends
        return prev

# R (Results):
#     - Example 1: Given list 1 -> 2 -> 3 -> 4 -> 5, the reversed list should be 5 -> 4 -> 3 -> 2 -> 1.
#     - Example 2: Given list 1 -> 2, the reversed list should be 2 -> 1.
#     - Example 3: Given an empty list (None), return None.

# E (Efficiency):
#     - Time Complexity: O(n), where n is the number of nodes in the list. We visit each node once.
#     - Space Complexity: O(1), since we are only using a constant amount of extra space (for `prev`, `current`, and `next_node` pointers).
