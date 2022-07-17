import time

class Timer:
    def __init__(self):
        self.start=0
        self.end=0

    def startTime(self):
        self.start=time.time()*1000

    def endTime(self):
        self.end=time.time()*1000

    def elapsed_time(self):
        return self.end-self.start

    def print(self):
        print("Took: {0}ms",self.elapsed_time())