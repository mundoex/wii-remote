import time

def clamp(value, min_value, max_value):
    return min(max(value, min_value),max_value)

def sign(num):
    return -1 if num<0 else 1

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
        print("Took: {0}ms".format(self.elapsed_time()))