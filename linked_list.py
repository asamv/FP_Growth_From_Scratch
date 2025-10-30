class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class linked_list :
    def __init__(self , first : Node = None, last :Node = None):
        self .first = first
        self.last = last
    
    def append(self, val):
        new_node = Node(val)
        if not self.first:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def display(self):
        current = self.first
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")