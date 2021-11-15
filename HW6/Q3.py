class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


# Class to create a Linked List
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # Print the linked list
    def print_list(self):
        if self.head == None:
            raise ValueError("List is empty")

        current = self.head
        while current:
            print(current.data, end="  ")
            current = current.next
        print("\n")
# Find length of Linked List
    def size(self):
        if self.head == None:
            return 0

        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next

        return size

    # Insert a node in a linked list
    def insert(self, data):
        node = Node(data)
        current = self.head
        if not current:
            self.head = node
        else:
            while (current.next):
                current = current.next
            current.next = node

    def sortList(self):  
        #Node current will point to head  
        current = self.head  
        point = None  
          
        if self.head == None:  
            return 
        else:  
            while current != None:  
                point = current.next 
                  
                while point != None:  
                    if current.data > point.data:  
                        temp = current.data
                        current.data = point.data 
                        point.data = temp  
                    point = point.next  
                current = current.next

first_node = Node(11)
linked_list = LinkedList(first_node)
linked_list.insert(3)
linked_list.insert(6)
print("The Linked List is:")
linked_list.print_list()

linked_list.sortList()
print("After sorting, the Linked List is:")
linked_list.print_list()