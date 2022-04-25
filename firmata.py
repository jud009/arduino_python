from pyfirmata import Arduino, util
import time

board = Arduino("/dev/cu.usbserial-RCBB_3B9700")
it = util.Iterator(board)
it.start()

LDR_SENSOR = board.get_pin('a:0:i')
RED_LED = board.get_pin('d:9:p')

NORMAL_LIGHT = 50
DARK_LIGHT = 80

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
    if (light >= NORMAL_LIGHT and light <= DARK_LIGHT):
        turnLedOn(0.05)
    elif (light >= DARK_LIGHT):
        turnLedOn(0.01)
    elif (light <= NORMAL_LIGHT):
        turnLedOn(10)

while True:
    checkLightAndTurnOnLed()
    time.sleep(1)
