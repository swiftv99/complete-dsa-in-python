"""
Merge Two Sorted Linked List
You are given the heads of two sorted linked lists list1 and list2. 
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.   

Example 1: 
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3: 
Input: list1 = [], list2 = [0]
Output: [0]

Constraints: 
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.val)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ptr1 = l1
        ptr2 = l2
        while ptr1 and ptr2:
            if ptr1.val >= ptr2.val:
                temp = ptr2.next
                ptr2.next = ptr1
                ptr2 = temp
            else:
                temp = ptr1.next
                ptr1.next = ptr2
                ptr1 = temp
        return l1 if l1.val >= l2.val else l2
    
def test(arr):
    linked_list = Solution()

    for elem in arr:
        linked_list.append(elem)
    return linked_list

linked_list1 = test([1,2,3,4])
print(linked_list1)
linked_list2 = test([1,3,4,5])
print(linked_list2)
obj = Solution()
