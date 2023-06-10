from Sensors import *
from CompositeLights import *
from Lights import Light
from Displays import *

class TrafficLights:
     def __init__(self):
        print("TrafficLightController: Constructor")
        self._number = 0
        self._display = LCDDisplay(sda = 20, scl = 21, i2cid = 0)
        self._lightRed = Light(0, "Red light")
        self._lightGreen = Light(1, "Green light")
        self._lightYellow = Light(3, "Yellow light")


# Turn Light red and display message on LCD screen   
     def redLight(self):
        print ("RED LIGHT **pedestrian crossing**  ")
        self._display.showText("RED LIGHT **pedestrian crossing**")
        print("=======================")
        self._lightRed.on()
        print("=======================")
        time.sleep(2)
        self._lightRed.off()

    # Turn lights green and display message on LCD screen
     def greenLight(self):
        print ("Green LIGHT **Car crossing**  ")
        self._display.showText("Green LIGHT **Car crossing**")
        print("=======================")
        self._lightGreen.on()
        print("=======================")
        time.sleep(2)
        self._lightGreen.off()

    # Flashes yellow light for emergency vehicle
     def yellowLight(self):
        print ("Caution Emergengy vehicle crossing")
        self._display.showText("Emergengy vehicle crossing")
        self._lightYellow.on()
        
        print("signal OFF")
