from evdev import UInput, ecodes as e

# Only way that worked to move mouse on ubuntu
class Mouse():
    def __init__(self):
        self.capabilities={
            e.EV_REL : (e.REL_X, e.REL_Y), 
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