"""
Middle of a Singly Linked List
Write a function to find and return the middle node of a singly linked list. If the list has an even number of nodes, 
return the second of the two middle nodes.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def find_middle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow 
    
"""
Time Complexity:
The time complexity is O(n), where n is the number of nodes in the linked list. This is because in the worst-case 
scenario, we have to traverse the whole linked list. Here, the 'fast' pointer is moving twice as fast as the 'slow' 
pointer, but it essentially goes through the entire list (or nearly the entire list in the case of an even number of 
nodes), so the time complexity is proportional to the size of the list, i.e., O(n).

Space Complexity:
The space complexity is O(1), which means that the space required does not change with the size of the input linked list, 
hence it's constant. This is because we are only using a fixed amount of space to store the 'slow' and 'fast' pointers, 
and we are not using any additional data structures like arrays or other linked lists whose size would scale with the 
input size. No matter how large the input linked list is, we only ever need two nodes ('slow' and 'fast') at any given 
time, so the space complexity is O(1).
"""