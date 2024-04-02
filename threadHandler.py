import threading
import queue
import time


class task:
    def __init__(self, func, conditions=None):
        self.func = func
        self.conditions = conditions

    def can_run(self):
        if self.conditions is None:
            return True
        return self.conditions()


class threadHandler:
    def __init__(self):
        self.task_queue = queue.Queue()
        self.is_running = False
        self.worker_thread = threading.Thread(target=self.process_queue)
        self.threads = []

    def add_task(self, task):
        self.task_queue.put(task)

    def process_queue(self):
        while self.is_running:
            if not self.task_queue.empty():
                task = self.task_queue.get()
                if task.can_run():
                    new_thread = threading.Thread(target=task.func)
                    new_thread.start()
                    self.threads.append(new_thread)
                else:
                    self.task_queue.put(task)
            self.remove_finished_threads()
            time.sleep(0.1)
            self.check_idle()

    def remove_finished_threads(self):
        self.threads = [thread for thread in self.threads if thread.is_alive()]

    def check_idle(self):
        #print(self.threads,self.task_queue.empty())
        return not self.threads and self.task_queue.empty()

    def start(self):
        self.is_running = True
        if not self.worker_thread.is_alive():
            self.worker_thread = threading.Thread(target=self.process_queue)
            self.worker_thread.start()

    def stop(self):
        self.is_running = False
        for thread in self.threads:
            thread.join()
        self.worker_thread.join()
