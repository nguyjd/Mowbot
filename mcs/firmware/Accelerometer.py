## @package mcs.firmware
# The lowest level of the mcs responsible for controling each components.

## @file Accelerometer.py
# Controls the wheel and blade motor relays.

import busio
import adafruit_lis331

## This class is used to control individual normally open relays.
# If the relay is enabled, a simple digital out is sent triggering a MOSFET controlled relay.
class Accelerometer:

    ##  Constructor for accelerometer module. 
    # Relays are normally open and disabled by default
    # @param sdaPin Raspberry Pi GPIO BCM pin number used for IC2(SDA)
    # @param sdlPin Raspberry Pi GPIO BCM pin number used for IC2(SDL)
    # @param debugFlag Boolean to indicate if debugging data should be printed
    # @param enabledFlag Boolean to indicate if opeations should be carried out.
    def __init__(self, sdaPin, sdlPin, debugFlag, enabledFlag):
        ## Boolean indicating if debug info should be included for this module
        self.debug = debugFlag

        ## Boolean to indicate if the accelermeter should be used.
        self.enabled = enabledFlag

        ## String for debugging
        self.debugPrefix = "[Accelerometer]"

        if self.enabled:
            self.debugPrefix += "[E]"
        else:
            self.debugPrefix += "[D]"

        self.i2c = busio.I2C(sdlPin, sdaPin)
        self.lis = adafruit_lis331.LIS331HH(self.i2c)

        if self.debug:
            print(self.debugPrefix + "[__init__()]: Using I2C Pins.")
            print(self.debugPrefix + "[__init__()]: Completed Setup of the accelerometer.")



    ## Return the reading from the acclerometer
    def GetReading(self):
        return self.lis.accleration