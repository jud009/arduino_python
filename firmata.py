from pyfirmata import Arduino, util
import time

board = Arduino("/dev/cu.usbserial-RCBB_3B9700") #trocar valor da porta
it = util.Iterator(board)
it.start()

LDR_SENSOR = board.get_pin('a:0:i')
RED_LED = board.get_pin('d:9:p')

NORMAL_LIGHT = 50
DARK_LIGHT = 70

def turnLedOn(light_Value):
    RED_LED.write(light_Value)

def getLightValue():
    sensor_value = LDR_SENSOR.read()
    if (sensor_value != None):
        light_value = sensor_value * 100
        return light_value
    return NORMAL_LIGHT

def checkLightAndTurnOnLed():
    light = getLightValue()
    print(light)
    if isMorning(light):
        turnLedOn(0)
    elif isLateAfternoon(light):
        turnLedOn(0.01)       
    elif isNight(light):
        turnLedOn(1)

def isMorning(light):
    return light <= NORMAL_LIGHT

def isLateAfternoon(light):
    return light >= NORMAL_LIGHT and light <= DARK_LIGHT

def isNight(light):
    return light >= DARK_LIGHT

while True:
    checkLightAndTurnOnLed()
    time.sleep(1)
