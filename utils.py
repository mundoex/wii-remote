import time
from tkinter import Message, Toplevel,Tk

def clamp(value, min_value, max_value):
    return min(max(value, min_value),max_value)

def sign(num):
    return -1 if num<0 else 1

def popup_window(title, message, timeout=1500):
    root = Tk()
    top = Toplevel()
    top.title(title)
    Message(top, text=message, padx=100, pady=100).pack()
    top.after(timeout, root.destroy)
    root.withdraw()
    root.mainloop()

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