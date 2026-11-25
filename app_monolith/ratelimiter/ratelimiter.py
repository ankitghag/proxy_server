class cratelimiter:
    def __init__(self, strategy):
        self.strategy= strategy
    def chk_allow(self):
        return self.strategy.allow()
