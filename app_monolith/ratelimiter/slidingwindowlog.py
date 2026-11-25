import time
class slidingwindowlog:
    def __init__(self):
        self.window_size= 30  
        self.limit= 2
        self.request_cnt= []
    def allow(self):
        rc= False
        current_time= time.time()
        window_start= current_time - self.window_size
        self.request_cnt= [ x  for x in self.request_cnt if x > window_start]
        if len(self.request_cnt) < self.limit:
            self.request_cnt.append(current_time)
            rc= True
        return rc

obj= slidingwindowlog()
print(obj.allow())
print(obj.allow())
print(obj.allow())
print(obj.allow())
time.sleep(30)
print(obj.allow())

