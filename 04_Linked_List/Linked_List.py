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
        result = ""
        temp_pointer = self.head
        while temp_pointer is not None:
            result += str(temp_pointer.value)
            if temp_pointer.next is not None:
                result += " -> "
            temp_pointer = temp_pointer.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_pointer = self.head
            for _ in range(index-1):
                temp_pointer = temp_pointer.next
            new_node.next = temp_pointer.next
            temp_pointer.next = new_node
        self.length += 1
        return True
    
    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
            
    def search(self, target):
        current = self.head
        index = 0
        while current:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1
            
    def get(self, index):
        if index == -1:
            return self.tail
        elif index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            prev = self.head
            while prev.next is not popped_node:
                prev = prev.next
            prev.next = None
            self.tail = prev
        self.length -= 1
        return popped_node
    
    def remove(self, index):
        if index < -1 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        if index == -1 or index == self.length - 1:
            return self.pop()
        prev = self.get(index-1)
        removed_node = prev.next
        prev.next = removed_node.next
        removed_node.next = None
        self.length -= 1
        return removed_node.value
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = -1
