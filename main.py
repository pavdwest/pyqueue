import dataclasses
import queue
import threading
import time
from dataclasses import dataclass

@dataclass
class Task:
    id: str

    def run(self, thread_number: int) -> int:
        print(f'[{str(self.__class__.__name__)}] Thread #{thread_number} is doing task #{self.id} in the queue.')


class TaskType2(Task):
    pass

class TaskType3(Task):
    pass


class WorkerPool:
    num_workers: int
    workers: list()

    def __init__(self, num_workers: int) -> None:
        self.num_workers = num_workers

    def start(self):
        for i in range(4):
            worker = threading.Thread(target=self.task_runner, args=(task_queue, i,), daemon=True)
            worker.start()

    def task_runner(self, q, thread_no):
        while True:
            task = q.get()
            time.sleep(2)
            task.run(thread_no)
            q.task_done()


# Create task queue
task_queue = queue.Queue()

# Create worker pool
wp = WorkerPool(num_workers=4)
wp.start()

# Create tasks
for j in range(5):
    t = Task(id=j)
    task_queue.put(t)

task_queue.join()

# Create more tasks
for j in range(5):
    t = TaskType2(id=j)
    task_queue.put(t)

task_queue.join()

# Create more tasks
for j in range(5):
    t = TaskType3(id=j)
    task_queue.put(t)

task_queue.join()
