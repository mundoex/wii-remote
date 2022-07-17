from enum import Enum
import cwiid
import time
from node_events import EventEmitter
from Tools import Timer
from Vector import Vector3
from WiiAcc import WiiAcc

REMOTE_BUTTONS=[
    cwiid.BTN_UP,
    cwiid.BTN_DOWN,
    cwiid.BTN_LEFT,
    cwiid.BTN_RIGHT,
    cwiid.BTN_A,
    cwiid.BTN_B,
    cwiid.BTN_MINUS,
    cwiid.BTN_HOME,
    cwiid.BTN_PLUS,
    cwiid.BTN_1,
    cwiid.BTN_2,
]

class WiiEvents(Enum):
    BTN_UP=str(cwiid.BTN_UP),
    BTN_DOWN=str(cwiid.BTN_DOWN),
    BTN_LEFT=str(cwiid.BTN_LEFT),
    BTN_RIGHT=str(cwiid.BTN_RIGHT),
    BTN_A=str(cwiid.BTN_A),
    BTN_B=str(cwiid.BTN_B),
    BTN_MINUS=str(cwiid.BTN_MINUS),
    BTN_HOME=str(cwiid.BTN_HOME),
    BTN_PLUS=str(cwiid.BTN_PLUS),
    BTN_1=str(cwiid.BTN_1),
    BTN_2=str(cwiid.BTN_2),
    #BTN_1 and BTN_2 have same mask as BTN_C and BTN_Z so different eventName
    BTN_C="nunchuk"+str(cwiid.NUNCHUK_BTN_C),
    BTN_Z="nunchuk"+str(cwiid.NUNCHUK_BTN_Z),
    ACC="acc",
    NUNCHUK_ACC="nunchukAcc",
    NUNCHUK_STICK="nunchukStick",
    LED_TURN_ON="ledOn",
    LED_TURN_OFF="ledOff",

REMOTE_EVENT_DIC={
    cwiid.BTN_UP: WiiEvents.BTN_UP,
    cwiid.BTN_DOWN: WiiEvents.BTN_DOWN,
    cwiid.BTN_LEFT: WiiEvents.BTN_LEFT,
    cwiid.BTN_RIGHT: WiiEvents.BTN_RIGHT,
    cwiid.BTN_A: WiiEvents.BTN_A,
    cwiid.BTN_B: WiiEvents.BTN_B,
    cwiid.BTN_MINUS: WiiEvents.BTN_MINUS,
    cwiid.BTN_HOME: WiiEvents.BTN_HOME,
    cwiid.BTN_PLUS: WiiEvents.BTN_PLUS,
    cwiid.BTN_1: WiiEvents.BTN_1,
    cwiid.BTN_2: WiiEvents.BTN_2,
}

class LedChangeState:
    def __init__(self, index, leds_state):
        self.index=index
        self.leds_state=leds_state

class WiiRemote:
    def __init__(self, input_poll_rate, sensitivity, starting_leds=0b0000):
        self.listener=EventEmitter()
        self.wii=None
        self.cached_leds=starting_leds
        self.input_poll_rate=input_poll_rate
        self.sensitivity=sensitivity
        self.running = False
        self.accHandler=WiiAcc(Vector3())

    def setupMode(self):    
        # Set read button accelerometer (nunchuk and IR enables nunchuck)
        print("Setting up mode")
        self.wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC | cwiid.RPT_NUNCHUK | cwiid.RPT_IR
        time.sleep(1)
        self.running=True

    def connect(self):
        while not self.wii: 
            try: 
                print("Attempting to connect")
                self.wii=cwiid.Wiimote()
                time.sleep(1)
                self.setupMode()
            except RuntimeError: 
                print("Failed to connect")
                time.sleep(1)
        print("Connected")

    def disconnect(self):
        self.running = False
        self.wii.led = 0
        self.wii = None

    def updateLeds(self):
        self.wii.led = self.cached_leds

    def turnOnLed(self, index):
        if(index <= 3 and index>=0):
            self.cached_leds |= self.cached_leds | (1 << index)
            self.updateLeds()
            ledState = LedChangeState(index, self.cached_leds)
            self.listener.emit(WiiEvents.LED_TURN_ON, ledState)
        else:
            raise Exception("Invalid index")
        
    def turnOffLed(self, index):
        if(index <= 3 and index>=0):
            self.cached_leds = self.cached_leds &~ (1 << index)
            self.updateLeds()
            ledState = LedChangeState(index, self.cached_leds)
            self.listener.emit(WiiEvents.LED_TURN_OFF, ledState)
        else:
            raise Exception("Invalid index")
    
    def flashLeds(self):
        for i in range(4):
            self.turnOnLed(i)
            time.sleep(0.1)
        for i in range(4):
            self.turnOffLed(i)
            time.sleep(0.1)

    def updateRemote(self):
        # Main remote buttons
        buttons = self.wii.state["buttons"]
        for remote_button in REMOTE_BUTTONS:
            is_btn_pressed = buttons & remote_button
            if is_btn_pressed:
                wii_event = REMOTE_EVENT_DIC[remote_button]
                self.listener.emit(wii_event, self)

        # Main accelerator
        acc = self.wii.state["acc"]
        self.accHandler.update(acc)
        self.listener.emit(acc)
        
    def updateNunchuk(self):
        nunchuk = self.wii.state["nunchuk"]
        # Check if nunchuk connected
        if nunchuk :    
            nunchuk_buttons=nunchuk["buttons"]
            nunchuk_stick=nunchuk["stick"]
            nunchuk_acc=nunchuk["acc"]

            # Nunchuk buttons
            is_btn_c_press = nunchuk_buttons & cwiid.NUNCHUK_BTN_C
            is_btn_z_press = nunchuk_buttons & cwiid.NUNCHUK_BTN_Z
            if is_btn_c_press:
                self.listener.emit(WiiEvents.BTN_C, self)
            if is_btn_z_press:
                self.listener.emit(WiiEvents.BTN_Z, self)
            
            # Nunchuk accelerator & stick
            self.listener.emit(WiiEvents.NUNCHUK_ACC, nunchuk_acc)
            self.listener.emit(WiiEvents.NUNCHUK_STICK, nunchuk_stick)

    def update(self):
        self.updateRemote()
        self.updateNunchuk()
       
    def run(self):
        next_loop_ms=time.time()*1000
        while self.running:
            
            # If it is time to execute tick
            while next_loop_ms < time.time()*1000:
                self.update()
                next_loop_ms+=self.input_poll_rate
                cur_time_ms=time.time()*1000

                # If next tick is in the future sleep until then
                if next_loop_ms > cur_time_ms : 
                    time.sleep((next_loop_ms-cur_time_ms)*0.001)



                
                






