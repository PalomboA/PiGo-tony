### GOPIGO AUTONOMOUS SCRIPT
### http://www.dexterindustries.com/GoPiGo/programming/python-programming-for-the-raspberry-pi-gopigo/

from gopigo import *
import time
STOP_DIST = 75

class Pigo:


    #####
    ##### BASIC STATUS AND METHODS
    #####

    status = {'ismoving' : False, 'servo' : 90, 'leftspeed' : 175,
              'rightspeed' : 175, 'dist': 100}

    def __init__(self):
        print "I'm a little robot car. Beep beep."
        self.checkDist()

    def stop(self):
        self.status["ismoving"] = False
        print "Stopping."
        for x in range(3):
            stop()

    def fwd(self):
        self.status["ismoving"] = True
        print "Let's get going."
        for x in range(3):
            fwd()

    def bwd(self):
        self.status["ismoving"] = True
        print "Let's back up."
        for x in range(3):
            bwd()

    # Check if the conditions are safe for the Pigo to continue
    def keepGoing(self):
        if self.status['dist'] < STOP_DIST:
            print "I think I see something in the distance."
            self.checkDist()
            if self.status['dist'] < STOP_DIST:
                print "Yep, there is for sure something big out there"
                return False
        elif volt() > 14 or volt() < 6:
            print "Voltage outside of safe range." + str(volt())
            return False
        else:
            return True

    def checkDist(self):
         self.status['dist'] = us_dist(15)
         print "I see something " + str(self.status['dist']) + "mm away."


    #####
    ##### COMPLEX METHODS
    #####

    def spin(self):
        right_rot()
        time.sleep(2)
        self.stop()

    def safeDrive(self):
        self.fwd()
        while self.keepGoing():
            self.checkDist()
        self.stop()

    def servoSweep(self):
        for ang in range(20, 160, 5):
            servo(ang)
            time.sleep(.1)

    def shakeServo(self):
        for x in range(10):
            if x % 2 == 0:
                servo(120)
                time.sleep(.1)
            else:
                servo(20)
                time.sleep(.1)

    def shuffle(self):
        for x in range(3):
            self.fwd()
            time.sleep(.5)
            self.bwd()
            time.sleep(.5)
            self.stop()

    def rturn(self):
        for x in range(3):
            right_rot()
        time.sleep(1)
        self.stop()

    def lturn(self):
        for x in range(3):
            left_rot()
        time.sleep(1)
        self.stop()

    def blink(self):
        for x in range(10):
            if x % 2 == 0:
                led_on(1)
                time.sleep(.1)
                led_off(1)
            else:
                servo(20)
                time.sleep(.1)

    def dance(self):
        print "I just want to spin!"
        self.spin()
        print "I just want to shuffle!"
        self.shuffle()
        print "I just want to shake my servo!"
        self.shakeServo()
        print "I just want to turn right!"
        self.rturn()
        print "I just want to turn left!"
        self.lturn()
        print "I just want to blink!"
        self.blink()
        print "I just want to shake my servo again!"
        self.shakeServo()


    #####
    ##### MAIN APP STARTS HERE
    #####
MaterPi = Pigo()

while MaterPi.keepGoing():
    MaterPi.checkDist()
### Put the method call after MaterPi here in order to tell the robot what to do.
    MaterPi.safeDrive()
    while MaterPi.keepGoing():
        MaterPi.checkDist()
    MaterPi.stop()

MaterPi.dance()

MaterPi.stop()

