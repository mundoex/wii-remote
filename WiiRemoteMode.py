from InputControl import Keyboard, Mouse
from SensitivyManager import SensitivityManager
from consts import VECTOR2D_DOWN, VECTOR2D_LEFT, VECTOR2D_RIGHT, VECTOR2D_UP
from utils import popup_window

class WiiRemoteMode():
    def __init__(self, name="Default", sensitivity=0.1):
        self.name=name
        self.sensitivity=sensitivity
        self.mouse=Mouse()
        self.keyboard=Keyboard()
        self.sense_manager=SensitivityManager(sensitivity)

    def onUp(self, remote):
        self.sense_manager.move(VECTOR2D_UP)
        (x,y)=self.sense_manager.direction_v2()
        self.mouse.move(0, y)

    def onDown(self, remote):
        self.sense_manager.move(VECTOR2D_DOWN)
        (x,y)=self.sense_manager.direction_v2()
        self.mouse.move(0, y)

    def onLeft(self, remote):
        self.sense_manager.move(VECTOR2D_LEFT)
        (x,y)=self.sense_manager.direction_v2()
        self.mouse.move(x, 0)

    def onRight(self, remote):
        self.sense_manager.move(VECTOR2D_RIGHT)
        (x,y)=self.sense_manager.direction_v2()
        self.mouse.move(x, 0)

    def onA(self, remote):
        self.mouse.click()

    def onB(self, remote):
        self.mouse.right_click()

    def onMinus(self, remote):
        pass

    def onHome(self, remote):
        pass

    def onPlus(self, remote):
        pass

    def on1(self, remote):
        self.keyboard.arrow_up()

    def on2(self, remote):
        self.keyboard.arrow_down()

    def onC(self, remote):
        pass

    def onZ(self, remote):
        pass

    def onAcc(self, remote):
        pass

    def onNunchukAcc(self, acc):
        pass

    def onNunchukStick(self, stick):
        pass

    def onTurnOnLed(self, ledChangeState):
        print("Led {0} On | State: {1}".format(ledChangeState.index, ledChangeState.leds_state))

    def onTurnOffLed(self, ledChangeState):
        print("Led {0} On | State: {1}".format(ledChangeState.index, ledChangeState.leds_state))

    def onConnected(self, remote):
        remote.turnOnLed(0)
        popup_window("Wii Remote","Wii Remote Connected")
        print("Connected")

    def onDisconnected(self, remote):
        popup_window("Wii Remote", "Wii Remote Disconnected")
        print("Disconnected")