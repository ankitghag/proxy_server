import time
class cfixedwindow:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0
        self.window = 0

    def allow(self):
        current_window = int(time.time()) // 60
        if current_window != self.window:
            self.window = current_window
            self.count = 0

        if self.count >= self.limit:
            return False

        self.count += 1
        return True
