"""
Remove Duplicates
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well. 

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        curr_node = head
        while curr_node and curr_node.next:
            if curr_node.val == curr_node.next.val:
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next
        return head        
        
"""
Time Complexity:
The time complexity is O(n), where n is the number of nodes in the linked list. This is because in the worst-case scenario, we have to traverse the entire linked list once. The while loop iterates through the list once, performing constant-time operations in each iteration.

Space Complexity:
The space complexity is O(1), which means that the space required does not change with the size of the input linked list
"""