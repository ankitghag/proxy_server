
import time


class TokenBucket:
    def __init__(self, capacity=10, refill_rate=10 / 60):
        self.capacity = capacity
        self.refill_rate = refill_rate  # tokens per second
        self.tokens = capacity
        self.last_refill_time = time.monotonic()

    def allow(self):
        current_time = time.monotonic()

        # 1. Calculate elapsed time
        elapsed_time = current_time - self.last_refill_time

        # 2. Refill tokens based on elapsed time
        new_tokens = elapsed_time * self.refill_rate

        self.tokens = min(self.capacity,self.tokens + new_tokens)

        # 3. Update refill timestamp
        self.last_refill_time = current_time

        # 4. Check whether a token is available
        if self.tokens >= 1:
            self.tokens -= 1
            return True

        return False

if __name__ = "__main__":
    limiter = TokenBucket(capacity=10, refill_rate=10 / 60)

    for i in range(12):
        print(i + 1, limiter.allow())





class token:
    def __init__(self):
        self.capacity= 10
        self.rate= 10/60
        self.tokens= self.capacity
        self.last_refill= time.monotonic()
    def allow():
        now= time.monotonic()
        elapsed= now - self.last_refill
        new_tokens= elapsed * self.rate
        self.tokens= min(self.capacity, self.tokens + new_tokens)
        if self.token >= 1:
            self.tokens-=1
            return True
        return False




