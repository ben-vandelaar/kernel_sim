import asyncio
import heapq
from task import KernelTask


class Kernel:

    def __init__(self):
        self.task_queue = asyncio.PriorityQueue()
        self.process_table = {}
        self.clock = 0
        self.next_pid = 0

    def spawn(self, coro, priority=0):
        pid = self.next_pid
        self.next_pid += 1

        task = KernelTask(pid, coro, priority)
        self.task_queue.put_nowait((priority, task))
        self.process_table[pid] = task
        return pid

    async def run(self):
        while not self.task_queue.empty():
            priority, task = await self.task_queue.get()
            try:
                task.step()
                self.task_queue.put_nowait((priority, task))
            except StopIteration:
                print(f"[Kernel] Process {task.pid} exited.")
                del self.process_table[task.pid]
