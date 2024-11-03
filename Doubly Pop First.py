class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__ (self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else :
            temp = self.head
            self.head = self.head.next
            # self.head = temp.next
            temp.next = None
            self.head.prev = None
        self.length -= 1
        return temp

my_linked_list = DoublyLinkedList(0)

# my_linked_list.append(1)
# my_linked_list.append(2)
# my_linked_list.append(3)

my_linked_list.pop_first()

my_linked_list.print_list()