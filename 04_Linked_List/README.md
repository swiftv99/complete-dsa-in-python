## **Linked List Basics**

### **Introduction**

This repository serves as a concise reference for understanding the fundamentals of linked lists in Python. Linked lists are an essential data structure in computer science, often used to dynamically manage memory and organize data. Unlike arrays, linked lists store elements as nodes, with each node pointing to the next, making insertion and deletion operations more efficient in certain scenarios.

### **Defining a Node**

A **node** is the basic building block of a linked list. Each node consists of:

1. **Value**: The data held by the node.
2. **Next**: A reference (or pointer) to the next node in the list, initialized as `None` for the last node.

Below is the implementation of a node in Python:

```python
class Node:
    def __init__(self, value):
        self.value = value  # The value of the node
        self.next = None    # Pointer to the next node, initially None
```

### **Building a Linked List**

A **linked list** is a collection of nodes connected sequentially. We'll cover how to:

1. Create a basic linked list.
2. Add new nodes to the list.
3. Traverse the list to access its elements.

```python
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
```

---

**\_\_str\_\_()** method

```python
def __str__(self):
    result = ""
    temp_pointer = self.head
    while temp_pointer is not None:
        result += str(temp_pointer.value)
        if temp_pointer.next is not None:
            result += " -> "
        temp_pointer = temp_pointer.next
    return result
```

---

**append()** method

```python
def append(self, value):
    new_node = Node(value)
    if self.length == 0:
        self.head = new_node
        self.tail = new_node
    else:
        self.tail.next = new_node
        self.tail = new_node
    self.length += 1
```

---

**prepend()** method

```python
def prepend(self, value):
    new_node = Node(value)
    if self.length == 0:
        self.head = new_node
        self.tail = new_node
    else:
        new_node.next = self.head
        self.head = new_node
    self.length += 1
```

---

**insert()** method

```python
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
```

---

**remove()** method

```python
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
```

---
