
import time

class slidingwindowcounter:
    def __init__(self, limit=10, window_size=60):
        self.limit = limit
        self.window_size = window_size
        self.clients = {}

    def allow(self, client_id):
        now = time.time()
        current_window = int(now // self.window_size)
        elapsed = now % self.window_size

        data = self.clients.get(client_id)

        if data is None:
            data = {"window": current_window, "previous": 0, "current": 0}
            self.clients[client_id] = data

        # Move counters when the fixed window changes
        if current_window != data["window"]:
            if current_window == data["window"] + 1:
                data["previous"] = data["current"]
            else:
                data["previous"] = 0
            data["current"] = 0
            data["window"] = current_window

        # Estimate requests in the rolling window
        previous_weight = (self.window_size - elapsed) / self.window_size
        estimated_count = (data["previous"] * previous_weight+ data["current"])
        if estimated_count >= self.limit:
            return False
        data["current"] += 1
        return True


limiter = SlidingWindowCounter(limit=10, window_size=60)
print(limiter.allow("user_1"))




class slide:
    def __init__(self):
        self.limit= 10
        self.window_size= 60
        self.clients= {}
    def allow(self, cid):
        now= time.time()
        current_window= int(now // self.window_size)
        we= now % self.window_size
        data= self.clients.get(cid)
        if data not in self.clients:
            data= {"window": current_window, "pc": 0, "cc": 0}
            self.clients[cid]= data
        if current_window != data["window"]:
            if current_window == data[window]+1:
                data["pc"]= data["cc"]
            else:
                data["pc"]= 0
            data["cc"]= 0
            data["window"]= current_window
        res= data["pc"] * (self.window_size - we / self.window_size) + data["cc"]
        if res >= self.limit:
            return False
        data["cc"]+=1
        return True



        





