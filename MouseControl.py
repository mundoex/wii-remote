from evdev import UInput, ecodes as e

# Only way that worked to move mouse on ubuntu
class Mouse():
    def __init__(self):
        self.capabilities={
            e.EV_REL : (e.REL_X, e.REL_Y), 
            e.EV_KEY : (e.BTN_LEFT, e.BTN_RIGHT),
        }
        self.ui = UInput(self.capabilities)

    def move(self,x,y):
        self.ui.write(e.EV_REL, e.REL_X, x)
        self.ui.write(e.EV_REL, e.REL_Y, y)
        self.ui.syn()