class Node(object):
    def __init__(self, data):
        self.data = data
        self.previous = None


# Class to create a Linked List
class LinkedList(object):
    def __init__(self, tail=None):
        self.tail = tail

    # Print the linked list
    def print_list(self):
        if self.tail == None:
            raise ValueError("List is empty")

        current = self.tail
        while current:
            print(current.data, end="  ")
            current = current.previous
        print("\n")
# Find length of Linked List
    def size(self):
        if self.tail == None:
            return 0

        size = 0
        current = self.tail
        while current:
            size += 1
            current = current.previous

        return size

    # Insert a node in a linked list
    def insert(self, data):
        node = Node(data)
        current = self.tail
        if not current:
            self.tail = node
        else:
            while (current.previous):
                current = current.previous
            current.previous = node

    def delete(self, data):
        if not self.tail:
            return

        temp = self.tail

        # Check if head node is to be deleted
        if self.tail.data == data:
            head = temp.previous
            print("Deleted node is " + str(self.tail.data))
            return

        while temp.previous:
            if temp.previous.data == data:
                print("Node deleted is " + str(temp.previous.data))
                temp.previous = temp.previous.previous
                return
            temp = temp.previous
        print("Node not found")
        return

    def search(self, x):
 
        # Initialize current to head
        current = self.tail
 
        # loop till current not equal to None
        while current != None:
            if current.data == x:
                return True # data found
             
            current = current.previous
         
        return False

first_node = Node(11)
linked_list = LinkedList(first_node)
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(5)

print("The Linked List is (after insertion):")
linked_list.print_list()

linked_list.delete(6)

print("The Linked List is (after deleting 6):")
linked_list.print_list()

print("Does 5 exist in the Linked List?")
print(linked_list.search(5))

print("Does 17 exist in the Linked List?")
print(linked_list.search(17))