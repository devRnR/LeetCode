class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.front_idx = 0
        self.rear_idx = 0
        self.size = 0
        self.max_size = k

        

    def enQueue(self, value: int) -> bool:
        if self.size == self.max_size:
            return False
        
        self.q[self.rear_idx] = value
        self.rear_idx = (self.rear_idx + 1) % self.max_size
        self.size += 1
    
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        
        value = self.q[self.front_idx]
        self.front_idx = (self.front_idx + 1) %self.max_size
        self.size -= 1
        return True
        

    def Front(self) -> int:
        if self.size == 0:
            return -1
        
        return self.q[self.front_idx]
        

    def Rear(self) -> int:
        if self.size == 0:
            return -1

        idx = (self.rear_idx - 1 + self.max_size) % self.max_size
        return self.q[idx]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()