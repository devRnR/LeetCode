class RecentCounter:

    def __init__(self):
        self.queue = []
    
    def ping(self, t: int) -> int:
        min = t - 3000
        max = t
        count = 1

        for q in self.queue:
            if max >= q >= min:
                count += 1
        
        self.queue.append(t)
    
        return count



        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)