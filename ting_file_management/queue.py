from collections import deque


class Queue:
    def __init__(self):
        self.data = deque()

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        return self.data.popleft()

    def search(self, index):
        if index < 0:
            raise IndexError("invalid index")
        return self.data[index]
