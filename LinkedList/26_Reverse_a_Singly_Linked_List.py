"""
Reverse a Singly Linked List
Write a function to reverse a singly linked list. The function should reverse the original linked list.

Example:
Original singly linked list:  1 -> 2 -> 3 -> 4 -> 5
Reversed singly linked list:  5 -> 4 -> 3 -> 2 -> 1
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
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def reverse(self):
        prev_node = None
        curr_node = self.head
        while curr_node is not None:
            temp = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp
        self.head, self.tail = self.tail, self.head
            
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(45)
print(linked_list)
linked_list.reverse()
print(linked_list)

"""
Overall, the time complexity for the entire reverse function is O(n) as it traverses all n nodes once, and the space 
complexity is O(1) as it uses a constant amount of space throughout its execution.
"""