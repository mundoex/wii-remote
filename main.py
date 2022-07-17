from Vector import Vector3
from Wii import WiiRemote, WiiEvents
from consts import WII_POLL_RATE
from MouseControl import Mouse

mouse=Mouse()
INPUT_POLL_RATE = 1
SENSITIVY = 1

def onUp(remote):
    SENSITIVY+=0.1
    print("up")

def onDown(remote):
    SENSITIVY-=0.1
    print("down")

def onLeft(remote):
    print("left")

def onRight(remote):
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
    print("Led {0} On | State: {1}",ledChangeState.index, ledChangeState.leds_state)

def onTurnOnOff(ledChangeState):
    print("Led {0} Off | State: {1}",ledChangeState.index, ledChangeState.leds_state)

def onAcc(acc):
    print("Acc", acc)
    v3=Vector3(acc)
    v2=v3.stereograhpic_projection()
    mouse.move(v2.x()*SENSITIVY, v2.y()*SENSITIVY)

def onNunchukAcc(acc):
    print("Nunchuk Acc", acc)

def onNunchukStick(stick):
    print("Nunchuk Stick", stick)

# Main
remote=WiiRemote(input_poll_rate=WII_POLL_RATE, sensitivity=SENSITIVY)
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