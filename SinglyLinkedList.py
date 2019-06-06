# A node
class Node:
    def __init__(self, data):
        self.item = data
        self.next = None


# LinkedList
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

# To print the data of all nodes
    def traverse(self):
        if self.head is None:
            print("Error: List is empty")
        else:
            crr = self.head
            count = -1
            # Traverse through list and print data until we get last node
            while crr is not None:
                count += 1
                print("(", count, ")", crr.item, "==>")
                crr = crr.next
            print(None)

# To add a node at the end of list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            # Traverse the list until we get the last node
            crr = self.head
            while crr.next is not None:
                crr = crr.next
            crr.next = new_node
            self.length += 1

# To add node at beginning of the list
    def prepend(self, data):
        # Simple, set new_node.next to head and new_node to head
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

# To add note after given item
    def insert_after_item(self, x, data):
        crr = self.head
        # Traverse through the list until we get the provided item
        while crr is not None:
            if crr.item == x:
                break
            crr = crr.next
        # But if crr wil be none, means item is not in the list
        if crr is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.next = crr.next
            crr.next = new_node
            self.length += 1

# To remove head node
    def remove_head(self):
        # Just update head to head.next
        if self.length == 0:
            print("Empty List")
        self.head = self.head.next
        self.length -= 1

# To remove last node
    def remove_last(self):
        if self.length == 0:
            print("Empty List!")
        # Maintain two nodes
        lastnode = self.head
        previousnode= self.head
        # Traverse until we get None
        while lastnode.next is not None:
            previousnode = lastnode
            lastnode = lastnode.next
        previousnode.next = None
        self.length -= 1

# To clear the list
    def clear_list(self):
        # If self.head is None means there is not next pointer
        self.head = None
