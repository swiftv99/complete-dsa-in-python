"""
Insertion at the Beginning of a Singly Linked List
Write a function to insert a new element at the beginning of a singly linked list. LinkedList and Node class are already provided.

Note: Function name must be prepend
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
        
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

linked_list = LinkedList()
linked_list.prepend(10)
print(linked_list.head.value)

"""
Time Complexity: O(1) 
Space Complexity: O(1)
"""