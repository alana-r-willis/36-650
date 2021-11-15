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
            
    def remove_dups(self):
 
        remove1 = None
        remove2 = None
        dup = None
        remove1 = self.head
 
        # Pick elements one by one
        while (remove1 != None and remove1.next != None):
 
            remove2 = remove1
 
            # Compare the picked element with rest
            # of the elements
            while (remove2.next != None):
 
                # If duplicate then delete it
                if (remove1.data == remove2.next.data):
 
                    # Sequence of steps is important here
                    dup = remove2.next
                    remove2.next = remove2.next.next
                else:
                    remove2 = remove2.next
 
            remove1 = remove1.next

first_node = Node(11)
linked_list = LinkedList(first_node)
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(3)
linked_list.insert(11)
linked_list.insert(6)
linked_list.insert(5)
linked_list.insert(7)
linked_list.insert(5)

print("The Linked List is:")
linked_list.print_list()

linked_list.remove_dups()
print("After removing the duplications, the Linked List is:")
linked_list.print_list()