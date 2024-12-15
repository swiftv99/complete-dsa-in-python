"""
Insertion at the End of a Singly Linked List
Write a method to insert a new element at the end of a singly linked list. The logic should cover edge cases such as empty linked list or linked list with some elements in it.
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
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
print(linked_list.head.next.value)

"""
Time Complexity: O(1) 
Space Complexity: O(1)
"""