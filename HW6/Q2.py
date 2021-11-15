class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def delete(self, item):
        return self.items.remove(item)

    def print(self):
      for e in self.items:
          print(e)

obj = Queue()
obj.enqueue(5)
obj.enqueue(7)
obj.enqueue(13)
obj.enqueue(4)
obj.enqueue(7)

print("The queue before delete:")
obj.print()

print("The queue after delete:")
obj.delete(7)
print(obj.dequeue())
obj.print()