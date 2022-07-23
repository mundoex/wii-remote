from evdev import UInput, ecodes as e
import time
from pynput.keyboard import Controller, Key
# Only way that worked to move mouse on ubuntu

KEY_PRESS_DELAY=0.1 #ms

class Keyboard():
    def __init__(self):
        self.keyboard=Controller()

    def arrow_down(self):
        self.keyboard.press(Key.down)
        time.sleep(KEY_PRESS_DELAY)
        self.keyboard.release(Key.down)
        time.sleep(KEY_PRESS_DELAY)

    def arrow_up(self):
        self.keyboard.press(Key.up)
        time.sleep(KEY_PRESS_DELAY)
        self.keyboard.release(Key.up)
        time.sleep(KEY_PRESS_DELAY)


class Mouse():
    def __init__(self):
        self.capabilities={
            e.EV_REL : (e.REL_X, e.REL_Y, e.REL_WHEEL),
            e.EV_KEY : (e.BTN_LEFT, e.BTN_RIGHT),
        }
        self.ui = UInput(self.capabilities)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.ui.close()

    def move(self, x, y):
        self.ui.write(e.EV_REL, e.REL_X, round(x))
        self.ui.write(e.EV_REL, e.REL_Y, round(y))
        self.ui.syn()
    
    def click(self):
        self.ui.write(e.EV_KEY, e.BTN_LEFT, 1)
        self.ui.syn()
        time.sleep(KEY_PRESS_DELAY)
        self.ui.write(e.EV_KEY, e.BTN_LEFT, 0)
        self.ui.syn()
        time.sleep(KEY_PRESS_DELAY)
        
    def right_click(self):
        self.ui.write(e.EV_KEY, e.BTN_RIGHT, 1)
        self.ui.syn()
        time.sleep(KEY_PRESS_DELAY)
        self.ui.write(e.EV_KEY, e.BTN_RIGHT, 0)
        self.ui.syn()
        time.sleep(KEY_PRESS_DELAY)