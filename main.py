from SensitivyManager import SensitivityManager
from Wii import WiiRemote, WiiEvents
from consts import VECTOR2D_DOWN, VECTOR2D_LEFT, VECTOR2D_RIGHT, VECTOR2D_UP, WII_POLL_RATE
from MouseControl import Mouse

mouse=Mouse()
SENSITIVY = 0.2
SENCE_MANAGER=SensitivityManager(SENSITIVY)

def onUp(remote):
    SENCE_MANAGER.move(VECTOR2D_UP)
    (x,y)=SENCE_MANAGER.direction_v2()
    mouse.move(0, y)
    print("up")

def onDown(remote):
    SENCE_MANAGER.move(VECTOR2D_DOWN)
    (x,y)=SENCE_MANAGER.direction_v2()
    mouse.move(0, y)
    print("down")

def onLeft(remote):
    SENCE_MANAGER.move(VECTOR2D_LEFT)
    (x,y)=SENCE_MANAGER.direction_v2()
    mouse.move(x, 0)
    print("left")

def onRight(remote):
    SENCE_MANAGER.move(VECTOR2D_RIGHT)
    (x,y)=SENCE_MANAGER.direction_v2()
    mouse.move(x, 0)
    print("right")

def onA(remote):
    print("a")

def onB(remote):
    print("b")

def on1(remote):
    print("1")

def on2(remote):
    print("2")

def onMinus(remote):
    print("minus")

def onHome(remote):
    print("home")

def onPlus(remote): 
    print("plus")

def onC(remote):
    print("c")

def onZ(remote):
    print("z")

def onTurnOnLed(ledChangeState):
    print("Led {0} On | State: {1}".format(ledChangeState.index, ledChangeState.leds_state))

def onTurnOnOff(ledChangeState):
    print("Led {0} On | State: {1}".format(ledChangeState.index, ledChangeState.leds_state))

def onAcc(acc):
    print("Acc", acc)

def onNunchukAcc(acc):
    print("Nunchuk Acc", acc)

def onNunchukStick(stick):
    print("Nunchuk Stick", stick)

# Main
remote=WiiRemote(input_poll_rate=WII_POLL_RATE)
remote.connect()

# Setup listeners
remote.listener.on(WiiEvents.BTN_UP, onUp)
remote.listener.on(WiiEvents.BTN_DOWN, onDown)
remote.listener.on(WiiEvents.BTN_LEFT, onLeft)
remote.listener.on(WiiEvents.BTN_RIGHT, onRight)
remote.listener.on(WiiEvents.BTN_A, onA)
remote.listener.on(WiiEvents.BTN_B, onB)
remote.listener.on(WiiEvents.BTN_MINUS, onMinus)
remote.listener.on(WiiEvents.BTN_HOME, onHome)
remote.listener.on(WiiEvents.BTN_PLUS, onPlus)
remote.listener.on(WiiEvents.BTN_1, on1)
remote.listener.on(WiiEvents.BTN_2, on2)
remote.listener.on(WiiEvents.BTN_C, onC)
remote.listener.on(WiiEvents.BTN_Z, onZ)

remote.listener.on(WiiEvents.ACC, onAcc)
remote.listener.on(WiiEvents.NUNCHUK_ACC, onNunchukAcc)
remote.listener.on(WiiEvents.NUNCHUK_STICK, onNunchukStick)

remote.listener.on(WiiEvents.LED_TURN_ON, onTurnOnLed)
remote.listener.on(WiiEvents.LED_TURN_OFF, onTurnOnOff)

remote.turnOnLed(0)
remote.run()