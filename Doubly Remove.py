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
    
    def get_value(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index <self.length / 2:
            for _ in range(index):
                temp = temp.next
        else :
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        before = self.get_value(index - 1)
        temp = before.next
        after = temp.next
        before.next = after
        after.prev = before

        # temp.next.prev = temp.prev
        # temp.prev.next = temp.next

        temp.prev = None
        temp.next = None
        self.length -= 1
        return temp

my_linked_list = DoublyLinkedList(0)

my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

my_linked_list.remove(1)

my_linked_list.print_list()
