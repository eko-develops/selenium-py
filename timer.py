import time


class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.elapsed_time = None

    def start(self):
        self.start_time = time.time()

    def end(self):
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time
