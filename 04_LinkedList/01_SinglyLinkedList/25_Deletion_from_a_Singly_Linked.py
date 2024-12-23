"""
Deletion from a Singly Linked List
Write a function to delete a node from a singly linked list and return deleted_node. The function should take the index(starting from 0) of the node to be deleted as a parameter.
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
    
    def remove(self, index):
        if index < 0 or index >= self.length or self.length == 0:
            return None
        elif index == 0:
            popped_node = self.head
            if self.length == 1:
                self.head = self.tail = None
            else:
                self.head = popped_node.next
                popped_node.next = None
            self.length -= 1
            return popped_node
        else:
            prev_node = self.head
            for _ in range(index-1):
                prev_node = prev_node.next
            
            removed_node = prev_node.next
            if removed_node.next is None:
                self.tail = prev_node
            prev_node.next = removed_node.next
            removed_node.next = None
            self.length -= 1
            return removed_node
        
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
print(linked_list.remove(4))

"""
Time Complexity:
The time complexity for removing a node from a singly linked list is O(n), where n is the length of the linked list. This 
is because in the worst-case scenario, you may have to traverse the entire list (when the node to remove is at the end of
the list, or the node does not exist).

Space Complexity:
The space complexity for this operation is O(1), which means it uses constant space. Despite the size of the linked list,
we only create two new variables (temp and popped_node), and we do not use any additional data structures that would grow 
with the size of the input.
"""