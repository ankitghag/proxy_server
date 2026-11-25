class cround_robin:
    def __init__(self):
        self.index= 0

    def select_server(self,servers):
        upstream= servers[self.index]
        self.index= (self.index + 1) % len(servers)
        return upstream
    



