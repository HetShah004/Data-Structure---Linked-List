# A node for Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# A doubly linked list
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        # Traverse through the list until we get None
        if self.head is None:
            print("List is empty")
            return
        crr = self.head
        while crr is not None:
            print(crr.data, "<>")
            crr = crr.next
        print(None)

    def insert_at_beginning(self, data):
        # A function which inserts only at head
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return
        print("List is not empty")

    def append(self, data):
        # Inserts node at end
        new_node = Node(data)
        crr = self.head
        if self.head is None:
            self.head = new_node
            return
        while crr.next is not None:
            crr = crr.next
        crr.next = new_node
        new_node.prev = crr

    def prepend(self, data):
        # Inserts node at beginning
        # If head is None, means the list is empty so we use "insert_at_beginning()"
        # Else we make next of new_node to head node and make new_node as head
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def search(self, data):
        # A loop is used and break when we get the data of that node
        # If we get the data provided, we stop loop and return True or print
        crr = self.head
        while crr.next is not None:
            if crr.data == data:
                break
            crr = crr.next
        if crr.data == data:
            print(f"{data} is in the list")
            return True
        else:
            print(f"{data} is not in the list")
            return False

    def remove_head(self):
        # Just make next of head as head and now previous of head to none which will
        # delete the old head node
        self.head = self.head.next
        self.head.prev = None

    def remove_tail(self):
        # Loop until we get the last node
        # Make next of previous node to None
        crr = self.head
        if self.head is None:
            print("List is empty")
            return
        while crr.next is not None:
            crr = crr.next
        crr.prev.next = None
