class Queue:
    def __init__(self):
        self._items = []

    def size(self):
        return len(self._items)
    
    def is_empty(self):
        return self.size() == 0

    def peek(self):
        if self.is_empty():
            return -1
        return self._items[0] 

    def enqueue(self, item):
        self._items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        self._items.pop(0)
 
    def clear(self):
        self._items.clear()
