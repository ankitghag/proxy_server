import datetime
from collection import deque
class cleakybucket:
    def __init__(self):
        self.capacity= 10
        self.last_leak= datetime.monotonic()
        self.leak_rate= 2
        self.reqq= deque()


    def allow():
        curr= datetime.monotonic()
        elpased= curr - self.last_leak
        leaked= int(elapsed * leak_rate)
        for _ in range(min(len(self.reqq), leaked)):
            self.reqq.popleft()
        if leaked > 0:
            self.last_leak+= leaked / leak_rate 
        if len(self.queue) >= self.capacity:
            retrun False
        self.reqq.append(now)
        return True



        
