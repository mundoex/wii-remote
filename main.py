import threading
from Wii import WiiRemote, WiiEvents
from WiiRemoteMode import WiiRemoteMode
from consts import WII_POLL_RATE
import time

def update_wii_remote_listeners(remote, wii_remote_mode):
    remote.listener.removeAllListeners()
    remote.listener.on(WiiEvents.BTN_UP, wii_remote_mode.onUp)
    remote.listener.on(WiiEvents.BTN_DOWN, wii_remote_mode.onDown)
    remote.listener.on(WiiEvents.BTN_LEFT, wii_remote_mode.onLeft)
    remote.listener.on(WiiEvents.BTN_RIGHT, wii_remote_mode.onRight)
    remote.listener.on(WiiEvents.BTN_A, wii_remote_mode.onA)
    remote.listener.on(WiiEvents.BTN_B, wii_remote_mode.onB)
    remote.listener.on(WiiEvents.BTN_MINUS, wii_remote_mode.onMinus)
    remote.listener.on(WiiEvents.BTN_HOME, wii_remote_mode.onHome)
    remote.listener.on(WiiEvents.BTN_PLUS, wii_remote_mode.onPlus)
    remote.listener.on(WiiEvents.BTN_1, wii_remote_mode.on1)
    remote.listener.on(WiiEvents.BTN_2, wii_remote_mode.on2)
    remote.listener.on(WiiEvents.ACC, wii_remote_mode.onAcc)

    remote.listener.on(WiiEvents.BTN_C, wii_remote_mode.onC)
    remote.listener.on(WiiEvents.BTN_Z, wii_remote_mode.onZ)
    remote.listener.on(WiiEvents.NUNCHUK_ACC, wii_remote_mode.onNunchukAcc)
    remote.listener.on(WiiEvents.NUNCHUK_STICK, wii_remote_mode.onNunchukStick)

    remote.listener.on(WiiEvents.LED_TURN_OFF, wii_remote_mode.onTurnOffLed)
    remote.listener.on(WiiEvents.LED_TURN_ON, wii_remote_mode.onTurnOnLed)
    
    remote.listener.on(WiiEvents.CONNECTED, wii_remote_mode.onConnected)
    remote.listener.on(WiiEvents.DISCONNECTED, wii_remote_mode.onDisconnected)

def wii_mote_heart_beat():
    print("Starting Wii remote heart beat")
    while True:
        if g_remote != None:
            if g_remote.wii != None:
                try:
                    g_remote.mutex.acquire()
                    g_remote.wii.request_status()
                    g_remote.bt_connection=True
                except :
                    g_remote.bt_connection=False
                    g_remote.disconnect()
                finally:
                    g_remote.mutex.release()
                    time.sleep(2)

g_remote=None
g_modes=[]
g_cur_mode=WiiRemoteMode()
heart_beat_thread=threading.Thread(target=wii_mote_heart_beat)

while True:
    if g_remote == None:
        g_remote=WiiRemote(input_poll_rate=WII_POLL_RATE)
        if not heart_beat_thread.is_alive():
            heart_beat_thread.start()
        update_wii_remote_listeners(g_remote, g_cur_mode)
    else:
        g_remote.connect()

    if g_remote.is_connected():
        g_remote.run()