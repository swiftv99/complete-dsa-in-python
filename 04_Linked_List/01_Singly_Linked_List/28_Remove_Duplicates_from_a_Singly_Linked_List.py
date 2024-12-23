"""
Remove Duplicates from a Singly Linked List
Given a singly linked list, write a function that removes all the duplicates. use this linked list .
Original Linked List - "1 -> 2 -> 4-> 3 -> 4->2"
Result Linked List - "1 -> 2 -> 4 -> 3
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
    
    def remove_duplicates(self):
        unique_set = set()
        prev_node = None
        curr_node = self.head
        while curr_node:
            next_node = curr_node.next
            if curr_node.value in unique_set:
                prev_node.next = next_node
                self.length -= 1
            else:
                unique_set.add(curr_node.value)
                prev_node = curr_node
            curr_node = next_node
        self.tail = prev_node
        
linked_list = LinkedList()
for i in range(0, 4):
    for _ in range(3-i, 4):
        linked_list.append(i+1)

print(linked_list)
print(linked_list.length)
linked_list.remove_duplicates()
print(linked_list)
print(linked_list.length)

"""
Overall, the time complexity of the remove_duplicates method is O(n), where n is the number of nodes in the linked list. 
This is because the while loop iterates through the list once, performing constant-time operations in each iteration. The 
space complexity of the remove_duplicates method is O(1), as the space used does not grow with the size of the input.
"""