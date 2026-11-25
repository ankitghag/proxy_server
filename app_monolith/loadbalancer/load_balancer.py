class cload_balancer:
    def __init__(self, strategy):
        self.strategy= strategy

    def get_server(self, servers):
        healthy_servers= [s for s in servers if s.health]
        # print(healthy_servers);
        if not healthy_servers:
            return None
        return self.strategy.select_server(healthy_servers)
    
    def decrease_index(self):
        self.strategy.index-= 1
        return 0
