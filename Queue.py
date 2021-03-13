class Queue:

    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display  the queue
    def display(self):
        #tempQ = Queue()
        for i in range(self.size()):
          #temp = self.dequeue()
          #tempQ.enqueue(temp)
          print(self.queue[i])
        #self.queue=tempQ.queue

    def size(self):
        return len(self.queue)

    def front(self):
        return self.queue[0]