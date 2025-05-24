class KernelTask:
    def __init__(self, pid, coro, priority):
        self.pid = pid
        self.coro = coro.__await__()
        self.priority = priority

    def step(self):
        next(self.coro)
