## @package hello
# Documentation for this module
#
# More details


import RPi.GPIO as GPIO


# module parameters
GEAR_RATIO = 26 # 26 motor rotations for one wheel rotation
INDEX_PULSE_PER_WHEEL_ROTATION = GEAR_RATIO # index will pulse 26 times per wheel rotation
INDEX_CHANGE_PER_WHEEL_ROTATION = 2 * GEAR_RATIO # 26 pulses = 52 state changes on pin
WHEEL_DIAMETER = 33 # diameter in cm
WHEEL_CIRCUMFERENCE = 3.14 * WHEEL_DIAMETER # circumference in cm
DISTANCE_PER_STEP = WHEEL_CIRCUMFERENCE / INDEX_CHANGE_PER_WHEEL_ROTATION # distance in cm for each step
DISTANCE_PER_STEP = 2 # above calculation yields 1.99



## This class is used to control and monitor a single encoder
# Enoceders may use up to 3 pins: Channels: X, A, B
# Various degrees of resolution are available
# Bewary of overloading Pi with aggressive resolution
# @author Keith
# @note 12/17/2020: Redeveloped due to data loss. -KS
class AMT103:

    ##  Constructor for relay control module. 
    # @param pinXNumber Interger Raspberry Pi GPIO BCM pin number used channel X of encoder
    # @param pinANumber Interger Raspberry Pi GPIO BCM pin number used channel X of encoder
    # @param pinBNumber Interger Raspberry Pi GPIO BCM pin number used channel X of encoder
    # @param highPrecision Boolean to indicate use of channel A for encoders
    # @param ultraPrecision Boolean to indicate use of channel A and B for encoders
    # @param directional Boolean to indicate if direction should be considered. Uess  channels A and B
    # @param debugFlag Boolean to indicate if debugging data should be printed
    # @param enabledFlag Boolean to indicate if opeations should be carried out.
    # @param debugName String to indicate name for debugging information
    def __init__(self, pinXNumber, pinANumber, debugFlag, enabledFlag, overrideFlag, debugName):
        ## Boolean indicating if debug info should be included for this module
        self.debug = debugFlag
        ## Boolean to indicate if this device should be used
        self.enabled = enabledFlag
        ## String to differentiate different relays for debugging
        self.debugPrefix = "[AMT103<" + debugName + ">]"
        if overrideFlag:
            self.debugPrefix += "[O]"
        if self.enabled:
            self.debugPrefix += "[E]"
        else:
            self.debugPrefix += "[D]"
        self.pinXNumber = pinXNumber
        self.pinANumber = pinANumber
        if self.enabled:
            GPIO.setup(pinXNumber, GPIO.IN)
            #GPIO.setup(pinANumber, GPIO.IN)
        if self.debug:
            print(self.debugPrefix + "[__init__()]: Channel X BCM pin = " + str(pinXNumber))
            #print(self.debugPrefix + "[__init__()]: Channel A BCM pin = " + str(pinANumber))

    ## Prints out encoder readings
    # Intended for testing only
    # Standard precision using channel X only
    def countDown(self, distance_cm):
        stepCount = int(distance_cm / DISTANCE_PER_STEP)
        if self.debug:
            print(self.debugPrefix + "[countDown()]: steps to target = " + str(stepCount))
        if self.enabled:
            oldX = GPIO.input(self.pinXNumber)
            while stepCount != 0:
                newX = GPIO.input(self.pinXNumber)
                if newX != oldX:
                    stepCount -= 1
                    oldX = newX
        print(self.debugPrefix + "[countDown()]: tagget reached")
                    
                    
